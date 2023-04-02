from pgzero.actor import Actor


class Base(Actor):
    def __init__(self, image, **kwargs):
        super().__init__(image, **kwargs)


class Bridge(Base):
    def __init__(self, **kwargs):
        super().__init__('bridge', **kwargs)


class Stone(Base):
    def __init__(self, **kwargs):
        super().__init__('stone', **kwargs)


class Tree(Base):
    def __init__(self, **kwargs):
        super().__init__('tree', **kwargs)


class Water(Base):
    def __init__(self, **kwargs):
        super().__init__('water', **kwargs)