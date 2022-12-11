from pgzero.actor import Actor


class Snowman(Actor):
    transparent_step = 2
    JUMP_HEIGHT = 200

    def __init__(self, image, **kwargs):
        super().__init__(image, **kwargs)
        self.is_moving_to_right = True
        self.is_jumping = False

    def jump(self, ground):
        if self.colliderect(ground):
            self.image = "snowman_up" if self.is_moving_to_right else 'snowman_up_left'
            self.is_jumping = True
