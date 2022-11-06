from typing import Tuple

import pygame
from pygame.surface import Surface


class Star:
    image: Surface
    position: Tuple[int, int]
    transparent_step = 2
    angle = 0

    def __init__(self, image, position):
        self.image = pygame.image.load(f"images/{image}").convert_alpha()
        self.position = position

    def change_transparency(self, is_fading):
        step = -self.transparent_step if is_fading else self.transparent_step
        self.image.set_alpha(self.image.get_alpha() + step)

    def rotate(self, angle):
        self.angle += angle
        self.image = pygame.transform.rotate(self.image, self.angle % 360)

        # self.position = self.image.get_rect(self.position).center
        # print(f"pos= {self.position}")
