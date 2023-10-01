import pygame
from pgzero.actor import Actor


class Base(Actor):
    def __init__(self, image, **kwargs):
        super().__init__(image, **kwargs)


class Bridge(Base):
    def __init__(self, **kwargs):
        super().__init__('bridge', **kwargs)


class Mountain(Base):
    def __init__(self, **kwargs):
        super().__init__('mountain', **kwargs)


class Tree(Base):
    def __init__(self, **kwargs):
        super().__init__('tree', **kwargs)


class Water(Base):
    def __init__(self, **kwargs):
        super().__init__('water', **kwargs)


class Stone(Base):
    def __init__(self, **kwargs):
        super().__init__('stone', **kwargs)


class Field(Base):
    def __init__(self, **kwargs):
        super().__init__('field', **kwargs)


class Monster(Actor):
    def __init__(self, images, **kwargs):
        super().__init__(images[0], **kwargs)
        self.direction = 1
        self.images = images
        self.current_image = 0
        self.is_hurt = False
        self.is_twincle = False
        self.life = 2

    def move(self, obstacles):
        self.x += self.direction
        for obstacle in obstacles:
            if obstacle.colliderect(self):
                self.direction *= -1
                self.x += self.direction
                self.current_image = (self.current_image + 1) % len(self.images)
                self.image = self.images[self.current_image]

    def hurt(self):
        if self.is_hurt:
            return
        self.is_hurt = True
        self.life -= 1
        print("I'm hurt")

    def stop_hurting(self):
        self.is_hurt = False

    def twincle(self):
        self.is_twincle = not self.is_twincle

class Attack(Actor):
    def __init__(self, **kwargs):
        super().__init__('fireball', **kwargs)
        self.is_hidden = True
        self.direction = pygame.Vector2()

    def hide(self):
        self.is_hidden = True

    def show(self):
        self.is_hidden = False

class Heart(Actor):

    def __init__(self, image, **kwargs):
        super().__init__(image, **kwargs)

