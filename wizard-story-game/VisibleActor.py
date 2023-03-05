import pgzero.actor
import pygame.display


class VisibleActor(pgzero.actor.Actor):
    def __init__(self, image: str, **kwargs):
        super().__init__(image, **kwargs)
        self.display_surface = pygame.display.get_surface()
        self.half_width = 1280 // 2  # self.display_surface.get_size()[0] // 2
        self.half_height = 768 // 2  # self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

    def draw_with_offset(self, player):
        self.offset.x = player.center[0] - self.half_width
        self.offset.y = player.center[1] - self.half_width
        offset_pos = self.topleft - self.offset
        self.topleft = offset_pos
        self.draw()


class Water(VisibleActor):
    def __init__(self, **kwargs):
        super().__init__('water', **kwargs)


class Bridge(VisibleActor):
    def __init__(self, **kwargs):
        super().__init__('bridge', **kwargs)


class Tree(VisibleActor):
    def __init__(self, **kwargs):
        super().__init__('tree', **kwargs)


class Stone(VisibleActor):
    def __init__(self, **kwargs):
        super().__init__('stone', **kwargs)