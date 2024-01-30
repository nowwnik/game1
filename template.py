import pygame

clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((1280, 720))
#убрать рамку flags=pygame.NOFRAME
pygame.display.set_caption("My game MF")
icon = pygame.image.load('images/1671710.jpg')
pygame.display.set_icon(icon)

square = pygame.Surface((50, 50))
square.fill('Blue')


background = pygame.image.load('images/background1.jpg')
run_right = [
    pygame.image.load('images/right/right_1.png'),
    pygame.image.load('images/right/right_2.png'),
    pygame.image.load('images/right/right_3.png'),
    pygame.image.load('images/right/right_4.png'),
]

run_left = [
    pygame.image.load('images/left/left_1.png'),
    pygame.image.load('images/left/left_2.png'),
    pygame.image.load('images/left/left_3.png'),
    pygame.image.load('images/left/left_4.png'),
]

player_animation_count = 0
bg_x = 0

background_sound = pygame.mixer.Sound('sounds/fon.mp3')
background_sound.play()

#game loop
running = True
while running:

    screen.blit(background,(bg_x, 0))
    screen.blit(background,(bg_x + 1280, 0))

    screen.blit(run_right[player_animation_count], (200, 500))
    if player_animation_count == 3:
        player_animation_count = 0
    else:
        player_animation_count += 1

    bg_x -= 7
    if bg_x == -1280:
        bg_x = 0
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    clock.tick(9)

