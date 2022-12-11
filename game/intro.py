import random
import pgzrun
import pygame

from game.coin import Coin
from snowman import Snowman

from pgzero.actor import Actor
from pgzero.animation import animate, decelerate
from pgzero.clock import clock
from pgzero.loaders import sounds, images
from pgzero.rect import Rect

score = 0

JUMP_HIGHT = 200

HEIGHT = 720  # ось Y
WIDTH = 1280  # ось X
PLAYER_IMAGE = 'snowman_right'
player = Snowman(PLAYER_IMAGE)
# circle._surf = pygame.transform.scale(circle._surf, (100, 100))
player.pos = 600, 500
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

torches = []
for i in range(3):
    torches.append(
        Actor('torch', bottomleft=(100+400 * i, HEIGHT - 100))
    )

coins = []
for i in range(20):
    coin = Coin(topleft=(random.randint(0, WIDTH - 100), random.randint(300, 600)))
    coins.append(coin)


def draw():
    global score
    screen.clear()
    sky_color = (sky_color_red, sky_color_green, sky_color_blue)
    screen.fill(sky_color)
    screen.draw.rect(ground, DARK_RED_COLOUR)

    for star in stars:
        star.draw()

    screen.blit('zima', (0, 0))

    for cloud in clouds:
        cloud.draw()

    for torch in torches:
        torch.draw()

    for coin in coins:
        coin.draw()

    player.draw()

    screen.draw.text(f"Счёт {score}", topleft=(50, 50), fontsize=70, color="#eab676", shadow=(1, 1), scolor="#e28743")


def update():
    global  ground, sky_color_blue, sky_color_red, sky_color_green, from_dark_to_light, score

    # sky
    if from_dark_to_light:
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
    if player.is_moving_to_right:
        player.x += step
    else:
        player.x -= step
    player_half_width = player.width / 2
    if player.x > WIDTH - player_half_width or player.x < player_half_width:
        player.is_moving_to_right = not player.is_moving_to_right
        flip_image()
    if not player.colliderect(ground) or player.is_jumping:
        if not player.is_jumping:
            player.y += step

        if player.y <= HEIGHT-100-JUMP_HIGHT:
            player.is_jumping = False
            player.image = 'snowman_down' if player.is_moving_to_right else 'snowman_down_left'
            print(f"player.is_moving_to_right {player.is_moving_to_right} {player.image}")
        else:
            player.y -= 2

    else:
        flip_image()

    for torch in torches:
        if player.colliderect(torch):
            set_player_hurt()

    for coin in coins:
        if player.colliderect(coin):
            coins.remove(coin)
            score += 100


def flip_image():
    if player.colliderect(ground):
        if player.is_moving_to_right:
            current_player_image = PLAYER_IMAGE
        else:
            current_player_image = "snowman_left"
        player.image = current_player_image


def on_mouse_down(pos):
    if player.collidepoint(pos):
        set_player_hurt()


def on_key_up(key):
    if key == keys.UP:
        player.jump(ground)


def set_player_hurt():
    player.image = 'snowman_hurt'
    # circle.angle += 180
    # circle.y -= 20
    clock.schedule_unique(set_player_normal, 0.2)


def set_player_normal():
    flip_image()
    player.angle = 0


pgzrun.go()
