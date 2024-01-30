import pygame

pygame.init()
screen = pygame.display.set_mode((600, 400))
#убрать рамку flags=pygame.NOFRAME
pygame.display.set_caption("My game MF")
icon = pygame.image.load('images/1671710.jpg')
pygame.display.set_icon(icon)

square = pygame.Surface((50, 50))
square.fill('Blue')

font = pygame.font.Font("fonts/Impact.ttf", 35)
text_surface = font.render('pidor', False, 'White')

player = pygame.image.load('images/1671710.jpg')

#game loop
running = True
while running:

    screen.blit(square, (0, 0))

    pygame.draw.circle(square, "Yellow", (45, 10), 5)

    screen.blit(text_surface, (100,100))
    screen.blit(player, (300,200))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()


