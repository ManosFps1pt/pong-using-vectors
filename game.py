from typing import Any
import pygame

pygame.init()
v2 = pygame.Vector2
screen = pygame.display.set_mode(v2(800, 600))
clock = pygame.time.Clock()
BASE_FPS = 60

class Pong(pygame.sprite.Sprite):
    def __init__(self, color: pygame.color.Color, pos: v2, key_up: int, key_down: int):
        super().__init__()
        
        self.position: v2 = pos
        self.velocity: v2 = v2(0, 0)
        self.acceleration: v2 = v2(0, 0)
        
        # constants
        self.VERTICAL_ACCELERATION = .2
        self.VERTICAL_FRICTION = .02

        self.key_up: int = key_up
        self.key_down: int = key_down
        self.image = pygame.Surface(v2(10, 100))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = pos

    def update(self):
        # set initial acceleration to 0, 0 to start
        self.acceleration = v2(0, 0)

        keys = pygame.key.get_pressed()
        up: bool = keys[self.key_up]
        down: bool = keys[self.key_down]
        if up:
            self.acceleration.y = - self.VERTICAL_ACCELERATION * delta_time
        elif down:
            self.acceleration.y = self.VERTICAL_ACCELERATION * delta_time
        
        self.acceleration.y -= self.velocity.y * self.VERTICAL_FRICTION
        self.velocity += self.acceleration
        self.position += self.velocity + .5 * self.acceleration
        
        self.rect.topleft = self.position
        
        


pongs = pygame.sprite.Group()
pong1 = Pong("#00ff00", v2(10, 0), pygame.K_UP, pygame.K_DOWN)



pongs.add(pong1)
run = True
while run:
    clock.tick()
    fps = clock.get_fps()
    try:
        delta_time = BASE_FPS / fps
    except ZeroDivisionError:
        delta_time = 1 / BASE_FPS

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.set_caption(f"{int(fps)}")
    screen.fill("#000000")

    pongs.update()
    pongs.draw(screen)

    pygame.display.update()



pygame.quit()

