from pgzero.actor import Actor


class Water(Actor):
    def __init__(self, **kwargs):
        super().__init__('water', **kwargs)