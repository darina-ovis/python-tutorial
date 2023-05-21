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

    def move(self, obstacles):
        self.x += self.direction
        for obstacle in obstacles:
            if obstacle.colliderect(self):
                self.direction *= -1
                self.x += self.direction
                self.current_image = (self.current_image + 1) % len(self.images)
                self.image = self.images[self.current_image]

