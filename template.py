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

player_speed = 10
player_x = 100
player_y = 500

is_jump = False
jump_count = 10

player_animation_count = 0
bg_x = 0

background_sound = pygame.mixer.Sound('sounds/fon.mp3')
#background_sound.play()

#game loop
running = True
while running:

    screen.blit(background,(bg_x, 0))
    screen.blit(background,(bg_x + 1280, 0))


    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        screen.blit(run_left[player_animation_count], (player_x, player_y))
    else:
        screen.blit(run_right[player_animation_count], (player_x, player_y))

    if keys[pygame.K_a] and player_x > 30:
        player_x -= player_speed
    elif keys[pygame.K_d] and player_x < 700:
        player_x += player_speed

    if not is_jump:
      if keys[pygame.K_SPACE]:
          is_jump = True
    else:
        if jump_count >= -10:
            if jump_count > 0:
                player_y -= (jump_count ** 2)/2
            else:
                player_y += (jump_count ** 2)/2
            jump_count -= 1
        else:
            is_jump = False
            jump_count = 10

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

    clock.tick(10)

