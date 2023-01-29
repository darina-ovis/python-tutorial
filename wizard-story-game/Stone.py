from pgzero.actor import Actor


class Stone(Actor):
    def __init__(self, **kwargs):
        super().__init__('stone', **kwargs)
