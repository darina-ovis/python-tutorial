import pgzrun
import pygame

from pgzero.actor import Actor
from pgzero.animation import animate, decelerate
from pgzero.clock import clock
from pgzero.loaders import sounds
from pgzero.rect import Rect

WIDTH = 1280  # ось X
HEIGHT = 720  # ось Y
CIRCLE_IMAGE = 'alien'
circle = Actor(CIRCLE_IMAGE)
# circle._surf = pygame.transform.scale(circle._surf, (100, 100))
circle.pos = 600, 500
is_moving_to_right = True

DARK_RED_COLOUR = 139, 0, 0
ground = Rect((0, HEIGHT - 100), (WIDTH, 100))


def draw():
    screen.clear()
    # screen.fill((red, 0, 100))
    screen.blit('background', (0, 0))

    screen.draw.filled_rect(ground, DARK_RED_COLOUR)
    circle.draw()


def update():
    global is_moving_to_right, ground
    step = 3
    if is_moving_to_right:
        circle.x += step
    else:
        circle.x -= step
    alien_half_width = circle.width / 2
    if circle.x > WIDTH - alien_half_width or circle.x < alien_half_width:
        is_moving_to_right = not is_moving_to_right
    if not circle.colliderect(ground):
        circle.y += step


def on_mouse_down(pos):
    if circle.collidepoint(pos):
        set_alien_hurt()


def on_key_up(key):
    if key == keys.RIGHT:
        circle.x += 10
    elif key == keys.DOWN:
        circle.x += 10
    if key == keys.UP:
        animate(circle, 'decelerate', 2, jump())


def jump():
    circle.y -= 50

def set_alien_hurt():
    circle.image = 'alien_hurt'
    circle.angle += 180
    circle.y -= 20
    sounds.eep.play()
    clock.schedule_unique(set_alien_normal, 0.2)


def set_alien_normal():
    circle.image = CIRCLE_IMAGE
    circle.angle = 0
    # circle._surf = pygame.transform.scale(circle._surf, (100, 100))
    print(ground.top)


pgzrun.go()
