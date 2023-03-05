import pygame
from pgzero.actor import Actor
from pgzero.keyboard import keys
from pygame.math import Vector2


class Player(Actor):
    def __init__(self, **kwargs):
        super().__init__('player', **kwargs)
        self.direction = pygame.Vector2()
        self.speed = 3

    def update_direction(self, key_pressed):
        if key_pressed == keys.UP:
            self.direction.y = -1
        elif key_pressed == keys.DOWN:
            self.direction.y = 1

        if key_pressed == keys.LEFT:
            self.direction.x = -1
        elif key_pressed == keys.RIGHT:
            self.direction.x = 1

    def move(self, obstacles):
        pos: Vector2
        if self.direction.magnitude() != 0:
            pos = self.direction.normalize() * self.speed
        else:
            pos = self.direction * self.speed

        self.x += pos.x

        for obstacle in obstacles:
            if self.colliderect(obstacle):
                if self.direction.x > 0:
                    self.right = obstacle.left
                elif self.direction.x < 0:
                    self.left = obstacle.right
                break

        self.y += pos.y
        for obstacle in obstacles:
            if self.colliderect(obstacle):
                if self.direction.y > 0:
                    self.bottom = obstacle.top
                elif self.direction.y < 0:
                    self.top = obstacle.bottom
                break

    def stop(self, key_pressed):
        if key_pressed in [keys.UP,  keys.DOWN]:
            self.direction.y = 0
        if key_pressed in [keys.LEFT,  keys.RIGHT]:
            self.direction.x = 0
