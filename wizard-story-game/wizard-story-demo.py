import pgzrun
import pygame
from pgzero import music

from Base import Bridge, Stone, Field, Base, Monster
from Base import Mountain
from Base import Tree
from Base import Water
from Player import Player
from Music import Music

HEIGHT = 768  # ось Y
WIDTH = 1280  # ось X
TILE = 64
# x - mountain
# r - river
# b - bridge
# t - tree
# f - field
# s - stone
# p - player
LEVEL_MAP = [
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'r', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x',
     'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'r', 'r', ' ', ' ', ' ', ' ', 't', ' ', 'fr', 'f', 'f',
     'f', 'fl', 't', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'r', 'r', ' ', ' ', ' ', ' ', 't', ' ', 'fr', 'f', 'f', 'f', 'fl', 't', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['x', ' ', ' ', ' ', ' ', 't', ' ', ' ', 't', ' ', ' ', ' ', 'r', 'r', ' ', ' ', ' ', ' ', 't', ' ', 'fr', 'f', 'f', 'f', 'fl', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', 't', ' ', 'x'],
    ['x', ' ', 't', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'r', 'r', ' ', ' ', 'm', ' ', 't', ' ', 'fr', 'f', 'f', 'f', 'fl', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', 't', ' ', 's', ' ', ' ', 'x'],
    ['x', ' ', ' ', ' ', 't', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'r', 'r', ' ', ' ', 's', ' ', ' ', ' ', 'fr', 'f', 'f', 'f', 'fl', 't', ' ', 't', 't', 't', 't', 't', 't', 'x', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['x', ' ', ' ', ' ', ' ', ' ', ' ', 't', ' ', ' ', ' ', ' ', 'r', 'r', ' ', ' ', ' ', ' ', ' ', ' ', 't', 't', 't', 't', 't', 't', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 't', ' ', ' ', ' ', 'x'],
    ['x', ' ', ' ', 't', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'r', 'r', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 't', ' ', ' ', 'x'],
    ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'bu', 'bu', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 's', ' ', 't', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 't', 'x'],
    ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 't', 'w', 'b', 'b', 'p', ' ', ' ', ' ', 't', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 't', ' ', 'x'],
    ['x', ' ', ' ', ' ', ' ', 't', ' ', ' ', ' ', ' ', ' ', ' ', 'bd', 'bd', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 't', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 's', 't', ' ', ' ', ' ', 'x'],
    ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'r', 'r', 'r', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 's', 'x'],
    ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'r', 'r', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'r', 'r', ' ', 's', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 's', ' ', 't', 'x'],
    ['x', ' ', ' ', 't', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'r', 'r', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 's', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 't', ' ', ' ', ' ', ' ', 'x'],
    ['x', ' ', ' ', ' ', ' ', ' ', ' ', 't', ' ', ' ', ' ', ' ', ' ', 'r', 'r', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'r', 'r', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 's', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'r', 'r', ' ', ' ', ' ', 't', ' ', ' ', 't', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 't', 's', 'x'],
    ['x', ' ', 't', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'r', 'r', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 's', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 't', ' ', ' ', ' ', 'r', 'r', 'r', 't', 't', 't', 't', 't', 't', 't', 't', 't', ' ', 't', ' ', 't', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 't', ' ', ' ', ' ', 'x'],
    ['x', ' ', ' ', ' ', 't', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'r', 'r', 'r', ' ', ' ', ' ', ' ', 't', 't', 't', 't', 't', ' ', 't', ' ', ' ', ' ', 't', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['x', ' ', ' ', ' ', ' ', ' ', 't', ' ', ' ', ' ', ' ', ' ', 'r', 'r', 'r', ' ', ' ', ' ', ' ', 't', 't', 't', 't', 't', ' ', 't', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 't', ' ', ' ', 'x'],
    ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'r', 'r', 'r', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 't', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 't', ' ', ' ', ' ', ' ', 'x'],
    ['x', ' ', ' ', 't', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'r', 'r', ' ', ' ', ' ', ' ', ' ', 't', 't', 't', 't', 't', 't', 't', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 's', 'x'],
    ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'r', 'r', ' ', ' ', ' ', ' ', ' ', 't', 't', 't', 't', 't', 't', 't', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'r', 'r', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
]

obstacles = []
visible = []
player: Player = None
monsters = []


def init():
    global player

    play_background_music()
    for y_index, row in enumerate(LEVEL_MAP):
        for x_index, col in enumerate(row):
            if col == 'x':
                mountain = Mountain(topleft=(x_index * TILE, y_index * TILE))
                obstacles.append(mountain)
                visible.append(mountain)
            elif col == 'p':
                player = Player(topleft=(x_index * TILE, y_index * TILE))
                visible.append(player)
            elif col == 't':
                tree = Tree(topleft=(x_index * TILE, y_index * TILE))
                visible.append(tree)
                obstacles.append(tree)
            elif col == 'r':
                river = Water(topleft=(x_index * TILE, y_index * TILE))
                visible.append(river)
                obstacles.append(river)
            elif col == 'b':
                bridge = Bridge(topleft=(x_index * TILE, y_index * TILE))
                visible.append(bridge)
            elif col == 'bu':
                bridge_up = Base('bw-up', topleft=(x_index * TILE, y_index * TILE))
                visible.append(bridge_up)
                obstacles.append(bridge_up)
            elif col == 'bd':
                bridge_down = Base('bw-dw', topleft=(x_index * TILE, y_index * TILE))
                visible.append(bridge_down)
                obstacles.append(bridge_down)
            elif col == 's':
                stone = Stone(topleft=(x_index * TILE, y_index * TILE))
                visible.append(stone)
            elif col == 'f':
                field = Field(topleft=(x_index * TILE, y_index * TILE))
                visible.append(field)
            elif col == 'fr':
                field_border = Base('grass-field-right', topleft=(x_index * TILE, y_index * TILE))
                visible.append(field_border)
            elif col == 'fl':
                field_border = Base('grass-field-left', topleft=(x_index * TILE, y_index * TILE))
                visible.append(field_border)
            elif col == 'm':
                snake = Monster(['snake'], topleft=(x_index * TILE, y_index * TILE))
                monsters.append(snake)
                visible.append(snake)
            elif col == 'w':
                wolf = Monster(['wolf-right', 'wolf-left'], topleft=(x_index * TILE, y_index * TILE))
                visible.append(wolf)
                monsters.append(wolf)
    if player is None:
        player = Player(topleft=(WIDTH // 2, HEIGHT // 2))
        visible.append(player)
    else:
        a = WIDTH // 2 - player.x
        b = HEIGHT // 2 - player.y

        for tile in visible:
            tile.x += a
            tile.y += b


def play_background_music():
    pygame.mixer.init()
    background_sound = pygame.mixer.Sound('music/background.wav')
    pygame.mixer.Channel(1).play(background_sound, -1)


init()


def is_tile_changed(current_tile) -> bool:
    return player.last_tile != current_tile and \
           (isinstance(player.last_tile, Bridge) or isinstance(player.last_tile, Field)
            or isinstance(current_tile, Bridge) or isinstance(current_tile, Bridge))


def change_music(current_tile):
    if isinstance(current_tile, Bridge):
        print('player on bridge')
        music.play('footsteps-on-bridge.wav')
    elif isinstance(current_tile, Field):
        print('player in mud')
        music.play('footsteps-on-ground.wav')
    else:
        print('player on grass')
        music.play('footsteps-on-grass.wav')


def draw():
    screen.clear()
    screen.fill('#228B22')
    for visible_object in sorted(visible,
                                 key=sorted_by_y_and_type()):
        visible_object.draw()
    current_tile = player.get_current_tile(visible)
    if not player.is_stopped() and is_tile_changed(current_tile):
        change_music(current_tile)
        player.last_tile = current_tile


def sorted_by_y_and_type():
    return lambda actor: actor.y if actor in obstacles or isinstance(actor, Player) or isinstance(actor, Monster) else 0


def update():
    global player, monsters, obstacles
    for monster in monsters:
        monster.move(obstacles)
    pos = player.get_offset(obstacles)
    visible.remove(player)
    for tile in visible:
        tile.x -= pos.x
        tile.y -= pos.y

    visible.append(player)


def on_key_down(key):
    global player
    if key == keys.SPACE:
        player.shoot(True)
        return

    player.update_direction(key)
    if not music.is_playing(''):
        change_music(player.last_tile)


def on_key_up(key):
    global player
    player.stop(key)
    if key == keys.SPACE:
        player.shoot(False)
    if player.is_stopped():
        music.stop()


pgzrun.go()
