from pgzero.actor import Actor
from pgzero.clock import clock
from pgzero.loaders import sounds

WIDTH = 1280  # ось X


class Snowman(Actor):
    JUMP_HEIGHT = 300
    PLAYER_IMAGE = 'snowman_right'
    STEP = 3

    def __init__(self, image, **kwargs):
        super().__init__(image, **kwargs)
        self.current_player_image = image

        self.is_moving_to_right = True
        self.is_jumping = False

        self.ground = kwargs.get("ground")

    def jump(self):
        if self.colliderect(self.ground):
            self.image = "snowman_up" if self.is_moving_to_right else 'snowman_up_left'
            self.is_jumping = True

    def set_hurt(self):
        self.image = 'snowman_hurt'
        clock.schedule_unique(self.set_normal, 0.2)

    def set_normal(self):
        self.flip_image()
        self.angle = 0

    def flip_image(self):
        if self.colliderect(self.ground):
            if self.is_moving_to_right:
                self.current_player_image = self.PLAYER_IMAGE
            else:
                self.current_player_image = "snowman_left"
            self.image = self.current_player_image

    def update_x(self):
        if self.is_moving_to_right:
            self.x += self.STEP
        else:
            self.x -= self.STEP
        player_half_width = self.width / 2
        if self.x > WIDTH - player_half_width or self.x < player_half_width:
            self.is_moving_to_right = not self.is_moving_to_right
            self.flip_image()
