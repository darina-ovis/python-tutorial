from pgzero.actor import Actor


class Snowman(Actor):
    transparent_step = 2
    PLAYER_IMAGE = 'snowman_right'

    def __init__(self, image, **kwargs):
        super().__init__(image, **kwargs)
        self.is_moving_to_right = True
        self.is_jumping = False
        self.player_half_width = self.width / 2
        self.ground = kwargs.get('ground')
        self.screen_width = kwargs.get('width')

    def jump(self, ground):
        if self.colliderect(ground):
            self.image = "snowman_up" if self.is_moving_to_right else 'snowman_up_left'
            self.is_jumping = True

    def move(self, is_moving_to_right: bool):
        if self.is_moving_to_right != is_moving_to_right:
            self.flip_image()
            self.is_moving_to_right = is_moving_to_right

        if self.x < (self.screen_width - self.player_half_width) and is_moving_to_right:
            self.x += 10

        if self.x > self.player_half_width and not is_moving_to_right:
            self.x -= 10

        if self.x > self.screen_width - self.player_half_width or self.x < self.player_half_width:
            self.is_moving_to_right = not self.is_moving_to_right
            self.flip_image()

    def flip_image(self):
        if self.colliderect(self.ground):
            if self.is_moving_to_right:
                current_player_image = self.PLAYER_IMAGE
            else:
                current_player_image = "snowman_left"
            self.image = current_player_image
