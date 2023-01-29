from pgzero.actor import Actor


class Player(Actor):
    def __init__(self, **kwargs):
        super().__init__('player', **kwargs)

