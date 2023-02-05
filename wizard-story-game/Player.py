import pygame
from pgzero.actor import Actor
from pgzero.keyboard import keys


class Player(Actor):
    def __init__(self, **kwargs):
        super().__init__('player', **kwargs)
        self.direction = pygame.Vector2()
        self.speed = 3

    def move(self, key_pressed):
        if key_pressed == keys.UP:
            self.direction.y = -1
        elif key_pressed == keys.DOWN:
            self.direction.y = 1
        # else:
        #     self.direction.y = 0

        if key_pressed == keys.LEFT:
            self.direction.x = -1
        elif key_pressed == keys.RIGHT:
            self.direction.x = 1
        # else:
        #     self.direction.x = 0

    def stop(self, key_pressed):
        if key_pressed in [keys.UP,  keys.DOWN]:
            self.direction.y = 0
        if key_pressed in [keys.LEFT,  keys.RIGHT]:
            self.direction.x = 0
