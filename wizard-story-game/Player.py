import pgzero
import pygame

from pgzero.keyboard import keys
from pygame.math import Vector2
from VisibleActor import VisibleActor


class Player(VisibleActor):
    def __init__(self, image: str, **kwargs):
        super().__init__(image, **kwargs)
        self.direction = pygame.Vector2()
        self.speed = 3
        self.hitbox = self._rect.inflate(0, -10)

    def update_direction(self, key_pressed):
        if key_pressed == keys.UP:
            self.direction.y = -1
        elif key_pressed == keys.DOWN:
            self.direction.y = 1

        if key_pressed == keys.LEFT:
            self.direction.x = -1
        elif key_pressed == keys.RIGHT:
            self.direction.x = 1

    def stop(self, key_pressed):
        if key_pressed in [keys.UP,  keys.DOWN]:
            self.direction.y = 0
        if key_pressed in [keys.LEFT,  keys.RIGHT]:
            self.direction.x = 0

    def move(self, obstacles):
        pos = self.calculate_next_pos()

        self.x += pos.x
        self.update_vertical_collision(obstacles)

        self.y += pos.y
        self.update_horizontal_collision(obstacles)

    def calculate_next_pos(self):
        pos: Vector2
        if self.direction.magnitude() != 0:
            pos = self.direction.normalize() * self.speed
        else:
            pos = self.direction * self.speed
        return pos

    def update_horizontal_collision(self, obstacles):
        for obstacle in obstacles:
            if self.colliderect(obstacle):
                if self.direction.y > 0:
                    self.bottom = obstacle.top
                elif self.direction.y < 0:
                    self.top = obstacle.bottom

    def update_vertical_collision(self, obstacles):
        for obstacle in obstacles:
            if self.colliderect(obstacle):
                if self.direction.x > 0:
                    self.right = obstacle.left
                elif self.direction.x < 0:
                    self.left = obstacle.right