from pgzero.actor import Actor


class Coin(Actor):

    def __init__(self, **kwargs):
        super().__init__('coin', **kwargs)

