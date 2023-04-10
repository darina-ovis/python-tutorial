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
            hitbox = obstacle.get_inflated()
            if self.colliderect(hitbox):
                if self.direction.y > 0:
                    self.bottom = hitbox.top
                elif self.direction.y < 0:
                    self.top = hitbox.bottom

    def update_vertical_collision(self, obstacles):
        for obstacle in obstacles:
            hitbox = obstacle.get_inflated()
            if self.colliderect(hitbox):
                if self.direction.x > 0:
                    self.right = hitbox.left
                elif self.direction.x < 0:
                    self.left = hitbox.right

   # def colliderect(self, *other):
   #      rect = self.__class__(*other)
   #      return (
   #          self.x < rect.x + rect.w and
   #          self.y < rect.y + rect.h and
   #          self.x + self.w > rect.x and
   #          self.y + self.h > rect.y
   #      )