from typing import Any
import pygame

# Set up the Pygame environment
# pygame 2.6.0, python 3.12.6

pygame.init()
v2 = pygame.Vector2
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode(v2(SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
BASE_FPS = 60


class Pong(pygame.sprite.Sprite):
    def __init__(self, color: pygame.Color, pos: v2, key_up: int, key_down: int):
        super().__init__()

        self.position: v2 = pos
        self.velocity: v2 = v2(0, 0)
        self.acceleration: v2 = v2(0, 0)

        # constants
        self.VERTICAL_ACCELERATION = .1
        self.VERTICAL_FRICTION = .005

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
        if self.rect.top < 0:
            self.rect.top = 0
            self.position = self.rect.topleft
        elif self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.position = self.rect.topleft


class Ball:
    def __init__(self, color: pygame.Color, size: int):
        self.color: pygame.Color = color
        self.size = size

        self.position = v2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.velocity = v2(0, 0)
        self.angle: int = 0
        self.speed: v2 = v2(0, 0)
        self.rect = pygame.Rect(self.position, (self.size, self.size))
        self.rect.center = self.position

    def update(self):

        pygame.draw.circle(screen, self.color, self.position, self.size)
        pygame.draw.rect(screen, "#00ff00", self.rect)


pongs = pygame.sprite.Group()
pong1 = Pong(pygame.color.Color("#aa0000"), v2(SCREEN_WIDTH - 20, 0), pygame.K_UP, pygame.K_DOWN)
pong2 = Pong(pygame.color.Color("#0000aa"), v2(10, 0), pygame.K_w, pygame.K_s)
ball = Ball(pygame.Color("#888888"), 10)

pongs.add(pong1)
pongs.add(pong2)
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

    ball.update()
    pongs.update()
    pongs.draw(screen)

    pygame.display.update()

pygame.quit()
