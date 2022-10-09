import pgzrun
from pgzero.actor import Actor
from pgzero.clock import clock
from pgzero.loaders import sounds

WIDTH = 900
HEIGHT = 600
alien = Actor('alien')
alien.pos = 100, 56
alien.topleft = 0, 450


def draw():
    screen.clear()
    screen.blit('background', (0, 0))
    alien.draw()


def update():
    alien.left += 2
    if alien.left > WIDTH:
        alien.right = 0


def on_mouse_down(pos):
    if alien.collidepoint(pos):
        set_alien_hurt()


def set_alien_hurt():
    alien.image = 'alien_hurt'
    alien.y -= 20
    sounds.eep.play()
    clock.schedule_unique(set_alien_normal, 0.2)


def set_alien_normal():
    alien.image = 'alien'
    alien.y += 20

pgzrun.go()
