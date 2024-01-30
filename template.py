import pygame
import random

WIDTH = 600 #ширина окна
HEIGHT = 400 #высота окна
FPS = 30 #фреймтайм

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)


pygame.init()
pygame.mixer.init() #звук
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("It's MY game MF")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
all_sprites.draw(screen)

#game loop
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
