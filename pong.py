import pygame

pygame.init()
v2 = pygame.Vector2

screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
base_fps = 60


class Paddle(pygame.sprite.Sprite):
    def __init__(self, pos: v2, size: v2, color: pygame.Color, keys: tuple[int, int]):
        super().__init__()
        self.pos: v2 = pos
        self.size: v2 = size
        self.color: pygame.Color = color
        self.image = pygame.Surface(size)
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos
        self.velocity = v2(0, 0)
        self.keys = keys

    def update(self):
        self.velocity.y = 0
        up_key = pygame.key.get_pressed()[self.keys[0]]
        down_key = pygame.key.get_pressed()[self.keys[1]]
        if up_key:
            self.velocity.y = -10 * delta_time
        if down_key:
            self.velocity.y = 10 * delta_time
        if up_key and down_key:
            self.velocity.y = 0
        self.pos += self.velocity
        self.rect.topleft = self.pos


pads = pygame.sprite.Group()
pad = Paddle(v2(100, 100), v2(100, 100), pygame.Color((50, 0, 0)), (pygame.K_UP, pygame.K_DOWN))
pads.add(pad)
print(pads)
while True:
    clock.tick(0)
    try:
        delta_time = base_fps / clock.get_fps()
    except ZeroDivisionError:
        delta_time = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.fill((50, 50, 50))
    pads.update()
    pads.draw(screen)
    pygame.display.set_caption(f"pong\tfps:\t{int(clock.get_fps())}\tdt:\t{delta_time}")
    pygame.display.update()

