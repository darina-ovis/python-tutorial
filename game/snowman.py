from pgzero import loaders
from pgzero.actor import Actor

class Snowman(Actor):
    transparent_step = 2

    is_moving_to_right = True
    is_jumping = False

    @property
    def image(self):
        return self._image_name

    @image.setter
    def image(self, image):
        self._image_name = image
        self._orig_surf = self._surf = loaders.images.load(image).convert_alpha()
        self._update_pos()

    def jump(self, ground):
        global is_jumping , is_moving_to_right
        if self.colliderect(ground) :
            self.image = "snowman_up" if self.is_moving_to_right else 'snowman_up_left'
            print(f"is_moving_to_right {self.is_moving_to_right} {self.image}")
            self.is_jumping = True
