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
    def __init__(self, image, **kwargs):
        super().__init__(image, **kwargs)
        self.counter = 0

    def move(self):
        self.x += 1 if self.counter < 50 else -1
        self.counter += 1
        if self.counter > 100:
            self.counter = 0
