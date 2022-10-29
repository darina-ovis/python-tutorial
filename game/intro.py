import random

import pgzrun
import pygame

from pgzero.actor import Actor
from pgzero.animation import animate, decelerate
from pgzero.clock import clock
from pgzero.loaders import sounds, images
from pgzero.rect import Rect

JUMP_HIGHT = 80

WIDTH = 1280  # ось X
HEIGHT = 720  # ось Y
CIRCLE_IMAGE = 'player_green'
player = Actor(CIRCLE_IMAGE)
# circle._surf = pygame.transform.scale(circle._surf, (100, 100))
player.pos = 600, 500
is_moving_to_right = True

sky_color_red = 0
sky_color_green = 0
sky_color_blue = 100
from_dark_to_light = True
DARK_RED_COLOUR = 139, 0, 0
ground = Rect((0, HEIGHT - 100), (WIDTH, 100))


stars = []
for i in range(30):
    stars.append(
        Actor('star', topleft=(random.randint(0, 200) * i, random.randint(0, 400)))
    )
clouds = []
for i in range(40):
    clouds.append(
        Actor('cloud' if i % 2 == 0 else 'cloud-2', topleft=(random.randint(100, 200) * i, random.randint(0, 400)))
    )

cactuses = []
for i in range(3):
    cactuses.append(
        Actor('cactus', bottomleft=(400 * i, HEIGHT - 100))
    )



def draw():
    screen.clear()
    sky_color = (sky_color_red, sky_color_green, sky_color_blue)
    screen.fill(sky_color)
    screen.blit('background_tr', (0, 0))
    screen.draw.rect(ground, DARK_RED_COLOUR)

    for star in stars:
        star.draw()
    for cloud in clouds:
        cloud.draw()

    for cactus in cactuses:
        cactus.draw()

    player.draw()


def update():
    global is_moving_to_right, ground, sky_color_blue, sky_color_red, sky_color_green, from_dark_to_light

    # sky
    if (from_dark_to_light):
        sky_color_blue = (sky_color_blue + 1) % 255
        sky_color_red = (sky_color_red + 1) % 255
        sky_color_green = (sky_color_green + 1) % 255
        if sky_color_green == 150:
            from_dark_to_light = False
    else:
        sky_color_blue = (sky_color_blue - 1) % 255
        sky_color_red = (sky_color_red - 1) % 255
        sky_color_green = (sky_color_green - 1) % 255
        if sky_color_green == 0:
            from_dark_to_light = True

    for cloud in clouds:
        if cloud.right <= 0:
            cloud.left = WIDTH
        if cloud.image == 'cloud':
            cloud.x -= 1
        else:
            cloud.x -= 2

    for star in stars:
        star.angle += 1


    # player
    step = 3
    if is_moving_to_right:
        player.x += step
    else:
        player.x -= step
    alien_half_width = player.width / 2
    if player.x > WIDTH - alien_half_width or player.x < alien_half_width:
        is_moving_to_right = not is_moving_to_right
    if not player.colliderect(ground):
        player.y += step


def on_mouse_down(pos):
    if player.collidepoint(pos):
        set_alien_hurt()


def on_key_up(key):
    if key == keys.RIGHT:
        player.x += 10
    elif key == keys.DOWN:
        player.x += 10
    if key == keys.UP:
        animate(player, 'decelerate', 2, jump())


def jump():
    if player.colliderect(ground):
        player.y -= JUMP_HIGHT


def set_alien_hurt():
    player.image = 'player_red'
    # circle.angle += 180
    # circle.y -= 20
    sounds.eep.play()
    clock.schedule_unique(set_alien_normal, 0.2)


def set_alien_normal():
    player.image = CIRCLE_IMAGE
    player.angle = 0
    # circle._surf = pygame.transform.scale(circle._surf, (100, 100))


pgzrun.go()
