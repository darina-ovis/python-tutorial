from pgzero.actor import Actor


class Bridge(Actor):
    def __init__(self, **kwargs):
        super().__init__('bridge', **kwargs)