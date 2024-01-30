import pygame

pygame.init()
screen = pygame.display.set_mode((600, 400))
#убрать рамку flags=pygame.NOFRAME
pygame.display.set_caption("My game MF")
icon = pygame.image.load('images/1671710.jpg')
pygame.display.set_icon(icon)

#game loop
running = True
while running:

    #screen.fill((255, 0, 0))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                screen.fill((255, 0, 0))


