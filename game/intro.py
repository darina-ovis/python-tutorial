import random
import pgzrun
import pygame
import time

from game.coin import Coin
from snowman import Snowman

from pgzero.actor import Actor
from pgzero.animation import animate, decelerate
from pgzero.clock import clock
from pgzero.loaders import sounds, images
from pgzero.rect import Rect

score = 0
time_life = 0
start_time = time.time()

JUMP_HEIGHT = 200

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
for i in range(10):
    torches.append(
        Actor('torch', bottomleft=(100+400 * i, HEIGHT - 100))
    )

hurt_torch = None
torch_fine = 0

coin_number = 20
def create_coins(n):
    global i
    for i in range(n):
        coin = Coin(topleft=(random.randint(0 , WIDTH - 100) , random.randint(300 , 600)))
        coins.append(coin)


coins = []
create_coins(coin_number)

def draw():
    global score, hurt_torch, time_life
    screen.clear()
    sky_color = (sky_color_red, sky_color_green, sky_color_blue)
    screen.fill(sky_color)
    screen.draw.rect(ground, DARK_RED_COLOUR)

    for star in stars:
        star.draw()

    screen.blit('fon_s_elkami', (0, 0))

    for cloud in clouds:
        cloud.draw()

    for torch in torches:
        torch.draw()

    if hurt_torch:
        screen.draw.text(f"-{torch_fine}", center=(hurt_torch.x, hurt_torch.y), fontsize=30, color="#eab676", shadow=(1, 1), scolor="#e28743")


    for coin in coins:
        coin.draw()

    player.draw()

    screen.draw.text(f"Счёт {score}", topleft=(50, 50), fontsize=70, color="#eab676", shadow=(1, 1), scolor="#e28743")
    if score < 0:
        screen.draw.text("Всё ты проиграл:(", center=(WIDTH/2, HEIGHT/2), fontsize=70, color="#eab676", shadow=(1, 1), scolor="#e28743")
        screen.draw.text(f"Время:{time_life} секунд(ы)", center=(WIDTH/2, HEIGHT/2 + 100), fontsize=70, color="#eab676", shadow=(1, 1), scolor="#e28743")


def update():
    global ground, sky_color_blue, sky_color_red, sky_color_green, from_dark_to_light, score, hurt_torch, torch_fine, coin_number, time_life, start_time

    if score < 0:
        if time_life == 0:
            time_life = round(time.time() - start_time)
        return

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
    max_height = HEIGHT - 100 - JUMP_HEIGHT
    velocity = (player.y - max_height)/4

    if not player.colliderect(ground) and not player.is_jumping:
        player.y += velocity

    if player.is_jumping:
        if round(player.y) <= HEIGHT-100-JUMP_HEIGHT:
            player.is_jumping = False
            player.image = 'snowman_down' if player.is_moving_to_right else 'snowman_down_left'
        else:
            player.y -= velocity
    else:
       flip_image()

    for torch in torches:
        torch.x -= 1
        if torch.x < 0:
            torch.x += 4000
        if player.colliderect(torch):
            set_player_hurt()
            score -= torch_fine
            torch_fine += 1
            hurt_torch = torch

    for coin in coins:
        if player.colliderect(coin):
            coins.remove(coin)
            score += 100
    if len(coins) == 0:
        if coin_number >= 2:
            coin_number -= 1
        else:
            coin_number = random.randint(1, 10)

        create_coins(coin_number)



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
    global score, start_time, time_life, torch_fine, player
    if key == keys.UP:
        player.jump(ground)

    if key == keys.SPACE and score <= 0:
        score = 0
        start_time = time.time()
        time_life = 0
        torch_fine = 0
        player.pos = 600, 450


def set_player_hurt():
    player.image = 'snowman_hurt'
    # circle.angle += 180
    # circle.y -= 20
    clock.schedule_unique(set_player_normal, 0.2)


def set_player_normal():
    global hurt_torch
    hurt_torch = None
    flip_image()
    player.angle = 0


pgzrun.go()
