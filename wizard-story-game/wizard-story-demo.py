import pgzrun
from pygame.math import Vector2

from Player import Player
from Stone import Stone
from Tree import Tree
from Water import Water
from Bridge import Bridge

HEIGHT = 768  # ось Y
WIDTH = 1280  # ось X
TILE = 64
# x - tree
# r - river
# p - player
LEVEL_MAP = [
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', ' ', 'r', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 't', 't', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['x', ' ', 'r', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 't', 't', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['x', ' ', 'b', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 't', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['x', ' ', 'b', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['x', 'r', 'r', 'p', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['x', 'r', 't', 't', 't', 't', 't', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['x', 'r', ' ', ' ', ' ', ' ', 't', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['x', 'r', ' ', ' ', ' ', ' ', 't', ' ', ' ', 't', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['r', 'r', ' ', ' ', ' ', ' ', 't', 't', 't', 't', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['r', 'r', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['r', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']
]

obstacles = []
visible = []
player: Player = None


def init():
    global player
    for y_index, row in enumerate(LEVEL_MAP):
        for x_index, col in enumerate(row):
            if col == 'x':
                stone = Stone(topleft=(x_index * TILE, y_index * TILE))
                obstacles.append(stone)
                visible.append(stone)
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


init()


def draw():
    screen.clear()
    screen.fill('#228B22')

    for visible_object in visible:
        visible_object.draw()


def update():
    global player, obstacles
    pos: Vector2
    if player.direction.magnitude() != 0:
        pos = player.direction.normalize() * player.speed
    else:
        pos = player.direction * player.speed

    player.pos += pos
    has_obstacle = False
    current_obstacle = None
    for obstacle in obstacles:
        if player.colliderect(obstacle):
            has_obstacle = True
            current_obstacle = obstacle
            break

    if has_obstacle:
        if player.direction.x == 1:
            player.right = current_obstacle.left
        elif player.direction.x == -1:
            player.left = current_obstacle.right
        if player.direction.y == 1:
            player.bottom = current_obstacle.top
        elif player.direction.y == -1:
            player.top = current_obstacle.bottom


def on_key_down(key):
    global player
    player.move(key)


def on_key_up(key):
    global player
    player.stop(key)


pgzrun.go()
