import pgzrun
from pgzero import music

from Base import Bridge, Stone, Field, Base
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
    ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'r', 'r', ' ', ' ', ' ', ' ', 't', ' ', 'f', 'f', 'f',
     'f', 'f', 't', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', 's', ' ', 'x'],
    ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'r', 'r', ' ', ' ', ' ', ' ', 't', ' ', 'f', 'f', 'f', 'f', 'f', 't', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['x', ' ', ' ', ' ', ' ', 't', ' ', ' ', 't', ' ', ' ', ' ', 'r', 'r', ' ', ' ', ' ', ' ', 't', ' ', 'f', 'f', 'f', 'f', 'f', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', 't', ' ', 'x'],
    ['x', ' ', 't', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'r', 'r', ' ', ' ', ' ', ' ', 't', ' ', 'f', 'f', 'f', 'f', 'f', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', 't', ' ', 's', ' ', ' ', 'x'],
    ['x', ' ', ' ', ' ', 't', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'r', 'r', ' ', ' ', 's', ' ', ' ', ' ', 'f', 'f', 'f', 'f', 'f', 't', ' ', 't', 't', 't', 't', 't', 't', 'x', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['x', ' ', ' ', ' ', ' ', ' ', ' ', 't', ' ', ' ', ' ', ' ', 'r', 'r', ' ', ' ', ' ', ' ', ' ', ' ', 't', 't', 't', 't', 't', 't', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 't', ' ', ' ', ' ', 'x'],
    ['x', ' ', ' ', 't', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'r', 'r', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 't', ' ', ' ', 'x'],
    ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'bu', 'bu', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 's', ' ', 't', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 't', 'x'],
    ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 't', ' ', 'b', 'b', ' ', ' ', ' ', ' ', 't', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 't', ' ', 'x'],
    ['x', ' ', ' ', ' ', ' ', 't', ' ', ' ', ' ', ' ', ' ', ' ', 'bd', 'bd', 'r', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 't', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 's', 't', ' ', ' ', ' ', 'x'],
    ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'r', 'r', 'r', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 's', 'x'],
    ['x', ' ', 'p', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'r', 'r', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
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


def init():
    global player
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
    if player is None:
        player = Player(topleft=(WIDTH // 2, HEIGHT // 2))
        visible.append(player)
    else:
        a = WIDTH // 2 - player.x
        b = HEIGHT // 2 - player.y
        # player.x = WIDTH // 2
        # player.y = HEIGHT // 2
        for tile in visible:
            tile.x += a
            tile.y += b


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
                                 key=lambda actor: actor.y if actor in obstacles or isinstance(actor, Player) else 0):
        visible_object.draw()
    current_tile = player.get_current_tile(visible)
    if not player.is_stopped() and is_tile_changed(current_tile):
        change_music(current_tile)
        player.last_tile = current_tile


def update():
    global player, obstacles
    pos = player.get_offset(obstacles)
    visible.remove(player)
    for tile in visible:
        tile.x -= pos.x
        tile.y -= pos.y

    visible.append(player)


def on_key_down(key):
    global player
    player.update_direction(key)
    if not music.is_playing(''):
        change_music(player.last_tile)


def on_key_up(key):
    global player
    player.stop(key)
    if player.is_stopped():
        music.stop()


pgzrun.go()
