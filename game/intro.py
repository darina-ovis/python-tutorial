import pgzrun
import pygame
from pgzero.actor import Actor
from pgzero.clock import clock
from pgzero.loaders import sounds

WIDTH = 1280 # ось X
HEIGHT = 720 # ось Y
CIRCLE_IMAGE = 'alien'
circle = Actor(CIRCLE_IMAGE)
# circle._surf = pygame.transform.scale(circle._surf, (100, 100))
circle.pos = (600, 500)
toRight = True

RED = 200, 0, 0
BOX = Rect((0, 620), (WIDTH, 100))


def draw():
    screen.clear()
    # screen.fill((red, 0, 100))
    screen.blit('background', (0, 0))
    screen.draw.rect(BOX, RED)

    circle.draw()


def update():
    global toRight, BOX

    step = 3
    if toRight:
        circle.x += step
    else:
        circle.x -= step
    alien_half_width = circle.width / 2
    if circle.x > WIDTH - alien_half_width or circle.x < alien_half_width:
         toRight = not toRight
    if not circle.colliderect(BOX):
        circle.y += 1


def on_mouse_down(pos):
    if circle.collidepoint(pos):
        set_alien_hurt()


def on_key_up(key):
    print(key)
    if key == keys.RIGHT:
        circle.x += 10
    elif key == keys.DOWN:
        circle.x += 10
    if key == keys.UP:
        circle.y -= 200

def set_alien_hurt():
    circle._surf = pygame.transform.rotate(circle._surf, 180)
    # circle._surf = pygame.transform.scale(circle._surf, (100, 100))
    circle.y -= 20
    sounds.eep.play()
    clock.schedule_unique(set_alien_normal, 0.2)

def set_alien_normal():
    circle._surf = pygame.transform.rotate(circle._surf, 180)
    # circle._surf = pygame.transform.scale(circle._surf, (100, 100))
    circle.y += 20

pgzrun.go()
