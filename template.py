import random

import pygame

clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((1280, 720))
# убрать рамку flags=pygame.NOFRAME
pygame.display.set_caption("POOP MASTER")
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

label = pygame.font.Font('fonts/Impact.ttf', 80)
lose_label = label.render('ЛОХ!', False, (255, 0, 0))
restar_label = label.render('не обосраться снова', False, (255, 100, 0))
restar_label_rect = restar_label.get_rect(topleft=(420, 300))

bullets_left = 5
bullet = pygame.image.load('images/bulet.png').convert_alpha()
bullets = []

gameplay = True

# game loop
running = True
while running:

    screen.blit(background, (bg_x, 0))
    screen.blit(background, (bg_x + 1280, 0))

    x = 0
    if gameplay:
        player_rect = run_left[0].get_rect(topleft=(player_x, player_y))

        if bullets_left > 0:
            for i in range(0,bullets_left):
                screen.blit(bullet, (x, 0))
                x += 45
                i+=1

        if poop_list:
            for (i, element) in enumerate(poop_list):
                screen.blit(poo, element)
                element.x -= 10

                if element.x < -10:
                    poop_list.pop(i)

                if player_rect.colliderect(element):
                    gameplay = False

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

        if pygame.mouse.get_pressed()[0] and bullets_left > 0:
            bullets.append(bullet.get_rect(topleft=(player_x + 30, player_y + 70)))

            bullets_left -= 1

        if bullets:
            for (i, element) in enumerate(bullets):
                screen.blit(bullet, (element.x, element.y))
                element.x += 10

                if element.x > 1280:
                    bullets.pop(i)

                if poop_list:
                    for (index, poop) in enumerate(poop_list):
                        if element.colliderect(poop):
                            poop_list.pop(index)
                            bullets.pop(i)

    else:
        screen.fill((0, 0, 0))
        screen.blit(lose_label, (440, 150))
        screen.blit(restar_label, restar_label_rect)

        mouse = pygame.mouse.get_pos()
        if restar_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            gameplay = True
            player_x = 100
            poop_list.clear()
            bullets.clear()
            bullets_left = 5

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
