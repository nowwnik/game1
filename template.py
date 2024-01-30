import random

import pygame

clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((1280, 720))
# убрать рамку flags=pygame.NOFRAME
pygame.display.set_caption("My game MF")
icon = pygame.image.load('images/1671710.jpg').convert()
pygame.display.set_icon(icon)

background = pygame.image.load('images/background1.jpg').convert_alpha()

poops = [
    pygame.image.load('images/poo/poo1.png').convert_alpha(),
    pygame.image.load('images/poo/poo2.png').convert_alpha(),
    pygame.image.load('images/poo/poo3.png').convert_alpha(),
    pygame.image.load('images/poo/poo4.png').convert_alpha(),
    pygame.image.load('images/poo/poo5.png').convert_alpha(),
    pygame.image.load('images/poo/poo6.png').convert_alpha(),
]

poo = random.choice(poops)

poop_list = []

run_right = [
    pygame.image.load('images/right/right_1.png').convert_alpha(),
    pygame.image.load('images/right/right_2.png').convert_alpha(),
    pygame.image.load('images/right/right_3.png').convert_alpha(),
    pygame.image.load('images/right/right_4.png').convert_alpha(),
]
run_left = [
    pygame.image.load('images/left/left_1.png').convert_alpha(),
    pygame.image.load('images/left/left_2.png').convert_alpha(),
    pygame.image.load('images/left/left_3.png').convert_alpha(),
    pygame.image.load('images/left/left_4.png').convert_alpha(),
]

player_speed = 10
player_x = 100
player_y = 500

is_jump = False
jump_count = 10

player_animation_count = 0
bg_x = 0

background_sound = pygame.mixer.Sound('sounds/fon.mp3')
# background_sound.play()

poop_timer = pygame.USEREVENT + 1
pygame.time.set_timer(poop_timer, 3500)

# game loop
running = True
while running:

    screen.blit(background, (bg_x, 0))
    screen.blit(background, (bg_x + 1280, 0))

    player_rect = run_left[0].get_rect(topleft=(player_x, player_y))

    if poop_list:
        for element in poop_list:
            screen.blit(poo, element)
            element.x -= 10

            if player_rect.colliderect(element):
                print("ты лох")

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
                player_y -= (jump_count ** 2) / 2
            else:
                player_y += (jump_count ** 2) / 2
            jump_count -= 1
        else:
            is_jump = False
            jump_count = 10

    if player_animation_count == 3:
        player_animation_count = 0
    else:
        player_animation_count += 1

    bg_x -= 8
    if bg_x == -1280:
        bg_x = 0

    # отрисовка
    pygame.display.update()
    # завершение
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == poop_timer:
            poop_list.append(poo.get_rect(topleft=(1200, 570)))
    # типа фреймтайм
    clock.tick(10)
