import random
import pgzrun
from pgzero.loaders import sounds

from snowman import Snowman

from pgzero.actor import Actor
from pgzero.rect import Rect

from game.star import Star

HEIGHT = 720  # ось Y
WIDTH = 1280  # ось X
DARK_RED_COLOUR = 139, 0, 0
ground = Rect((0, HEIGHT - 100), (WIDTH, 100))
player = Snowman('snowman_right', ground=ground)

player.pos = 100, 600
sky_color_red = 0
sky_color_green = 0
sky_color_blue = 100
from_dark_to_light = True

points = 300

stars = []
for i in range(30):
    stars.append(Star('star.png', (random.randint(0, 200) * i, random.randint(0, 400))))

clouds = []
for i in range(40):
    clouds.append(
        Actor('cloud' if i % 2 == 0 else 'cloud-2', topleft=(random.randint(100, 200) * i, random.randint(0, 400)))
    )

torches = []
for i in range(30):
    torches.append(
        Actor('torch', bottomleft=(200 + 400 * i, HEIGHT - 100))
    )


def draw():
    screen.clear()
    sky_color = (sky_color_red, sky_color_green, sky_color_blue)
    screen.fill(sky_color)
    screen.draw.rect(ground, DARK_RED_COLOUR)

    for star in stars:
        screen.blit(star.image, star.position)

    screen.blit('zima', (0, 0))

    for cloud in clouds:
        cloud.draw()

    for torch in torches:
        torch.draw()

    player.draw()
    screen.draw.text(f"Score: {points}", midleft=(50, 50), fontsize=50, shadow=(2, 2), scolor="#202020")

    if points <= 0:
        screen.draw.text("Game Over", center=(WIDTH/2, HEIGHT/2), fontsize=70, shadow=(2, 2), scolor="#202020")



def update():
    global ground, sky_color_blue, sky_color_red, sky_color_green, from_dark_to_light, points

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
        star.change_transparency(from_dark_to_light)

    # player
    # player.update_x()

    height_y = 5 * player.y / (HEIGHT - 100 - player.JUMP_HEIGHT)
    if player.is_jumping:
        if player.y <= HEIGHT - 100 - player.JUMP_HEIGHT:
            player.is_jumping = False
            player.image = 'snowman_down' if player.is_moving_to_right else 'snowman_down_left'
        else:
            player.y -= height_y

    if not player.colliderect(ground):
        if not player.is_jumping:
            player.y += height_y
    else:
        player.flip_image()

    if points > 0:
        for torch in torches:
            torch.x -= 2
            if player.colliderect(torch):
                player.set_hurt()
                sounds.eep.play()
                points -= 1


def on_mouse_down(pos):
    if player.collidepoint(pos):
        player.set_hurt()


def on_key_up(key):
    if key == keys.UP or keys.SPACE :
        player.jump()


pgzrun.go()
