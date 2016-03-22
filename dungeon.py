import random

GRID1 = [(0,0), (0,1), (0,2),
         (1,0), (1,1), (1,2),
         (2,0), (2,1), (2,2)]

GRID2 = [(0,0), (0,1), (0,2), (0,3),
         (1,0), (1,1), (1,2), (1,3),
         (2,0), (2,1), (2,2), (2,3),
         (3,0), (3,1), (3,2), (3,3)]

GRID3 = [(0,0), (0,1), (0,2), (0,3), (0,4),
         (1,0), (1,1), (1,2), (1,3), (1,4),
         (2,0), (2,1), (2,2), (2,3), (2,4),
         (3,0), (3,1), (3,2), (3,3), (3,4),
         (4,0), (4,1), (4,2), (4,3), (4,4)]

GRID4 = [(0,0), (0,1), (0,2), (0,3), (0,4), (0,5),
         (1,0), (1,1), (1,2), (1,3), (1,4), (1,5),
         (2,0), (2,1), (2,2), (2,3), (2,4), (2,5),
         (3,0), (3,1), (3,2), (3,3), (3,4), (3,5),
         (4,0), (4,1), (4,2), (4,3), (4,4), (4,5),
         (5,0), (5,1), (5,2), (5,3), (5,4), (5,5)]

GRID5 = [(0,0), (0,1), (0,2), (0,3), (0,4), (0,5), (0,6),
         (1,0), (1,1), (1,2), (1,3), (1,4), (1,5), (1,6),
         (2,0), (2,1), (2,2), (2,3), (2,4), (2,5), (2,6),
         (3,0), (3,1), (3,2), (3,3), (3,4), (3,5), (3,6),
         (4,0), (4,1), (4,2), (4,3), (4,4), (4,5), (4,6),
         (5,0), (5,1), (5,2), (5,3), (5,4), (5,5), (5,6),
         (6,0), (6,1), (6,2), (6,3), (6,4), (6,5), (6,6)]

GRID6 = [(0,0), (0,1), (0,2), (0,3), (0,4), (0,5), (0,6), (0,7),
         (1,0), (1,1), (1,2), (1,3), (1,4), (1,5), (1,6), (1,7),
         (2,0), (2,1), (2,2), (2,3), (2,4), (2,5), (2,6), (2,7),
         (3,0), (3,1), (3,2), (3,3), (3,4), (3,5), (3,6), (3,7),
         (4,0), (4,1), (4,2), (4,3), (4,4), (4,5), (4,6), (4,7),
         (5,0), (5,1), (5,2), (5,3), (5,4), (5,5), (5,6), (5,7),
         (6,0), (6,1), (6,2), (6,3), (6,4), (6,5), (6,6), (6,7),
         (7,0), (7,1), (7,2), (7,3), (7,4), (7,5), (7,6), (7,7)]

GRID7 = [(0,0), (0,1), (0,2), (0,3), (0,4), (0,5), (0,6), (0,7), (0,8),
         (1,0), (1,1), (1,2), (1,3), (1,4), (1,5), (1,6), (1,7), (1,8),
         (2,0), (2,1), (2,2), (2,3), (2,4), (2,5), (2,6), (2,7), (2,8),
         (3,0), (3,1), (3,2), (3,3), (3,4), (3,5), (3,6), (3,7), (3,8),
         (4,0), (4,1), (4,2), (4,3), (4,4), (4,5), (4,6), (4,7), (4,8),
         (5,0), (5,1), (5,2), (5,3), (5,4), (5,5), (5,6), (5,7), (5,8),
         (6,0), (6,1), (6,2), (6,3), (6,4), (6,5), (6,6), (6,7), (6,8),
         (7,0), (7,1), (7,2), (7,3), (7,4), (7,5), (7,6), (7,7), (7,8),
         (8,0), (8,1), (8,2), (8,3), (8,4), (8,5), (8,6), (8,7), (8,8)]

GRID8 = [(0,0), (0,1), (0,2), (0,3), (0,4), (0,5), (0,6), (0,7), (0,8), (0,9),
         (1,0), (1,1), (1,2), (1,3), (1,4), (1,5), (1,6), (1,7), (1,8), (1,9),
         (2,0), (2,1), (2,2), (2,3), (2,4), (2,5), (2,6), (2,7), (2,8), (2,9),
         (3,0), (3,1), (3,2), (3,3), (3,4), (3,5), (3,6), (3,7), (3,8), (3,9),
         (4,0), (4,1), (4,2), (4,3), (4,4), (4,5), (4,6), (4,7), (4,8), (4,9),
         (5,0), (5,1), (5,2), (5,3), (5,4), (5,5), (5,6), (5,7), (5,8), (5,9),
         (6,0), (6,1), (6,2), (6,3), (6,4), (6,5), (6,6), (6,7), (6,8), (6,9),
         (7,0), (7,1), (7,2), (7,3), (7,4), (7,5), (7,6), (7,7), (7,8), (7,9),
         (8,0), (8,1), (8,2), (8,3), (8,4), (8,5), (8,6), (8,7), (8,8), (8,9),
         (9,0), (9,1), (9,2), (9,3), (9,4), (9,5), (9,6), (9,7), (9,8), (9,9)]

GRIDS = [GRID1, GRID2, GRID3, GRID4, GRID5, GRID6, GRID7, GRID8]

def get_locations(level):

    monster = random.choice(GRIDS[level-1])
    start = random.choice(GRIDS[level-1])
    door = random.choice(GRIDS[level-1])
    if monster == door or monster == start or door == start:
        return get_locations(level-1)

    return monster, door, start



def move_player(player, move):
    x, y = player

    if move == 'LEFT':
        y -= 1
    elif move == 'RIGHT':
        y += 1
    elif move == 'UP':
        x -= 1
    elif move == 'DOWN':
        x += 1

    return x,y

def move_monster(monster, door, player):
    #get door location
    a, b = player
    c, d = door

    #get monster location
    i, j = monster
    #move closer to door
    if c > i:
        i += 1
    elif c < i:
        i -= 1
    elif d > j:
        j += 1
    elif d < j:
        j -= 1
    else:
        i, j

    return i, j

def get_moves(player, level):
    moves = ['LEFT', 'RIGHT', 'UP', 'DOWN']

    if player[1] == 0:
        moves.remove('LEFT')
    if player[1] == 2 and level == 1 or player[1] == 3 and level == 2 or player[1] == 4 and level == 3 or player[1] == 5 and level == 4 or player[1] == 6 and level == 5 or player[1] == 7 and level == 6 or player[1] == 8 and level == 7 or player[1] == 9 and level == 8:
        moves.remove('RIGHT')
    if player[0] == 0:
        moves.remove('UP')
    if player[0] == 2 and level == 1 or player[0] == 3 and level == 2 or player[0] == 4 and level == 3 or player[0] == 5 and level == 4 or player[0] == 6 and level == 5 or player[0] == 7 and level == 6 or player[0] == 8 and level == 7 or player[0] == 9 and level == 8:
        moves.remove('DOWN')

    return moves

def draw_map(player, level):
    tile = '|{}'
    indices = [[0,1,3,4,6,7],
               [0,1,2,4,5,6,8,9,10,12,13,14],
               [0,1,2,3,5,6,7,8,10,11,12,13,15,16,17,18,20,21,22,23],
               [0,1,2,3,4,  6,7,8,9,10, 12,13,14,15,16, 18,19,20,21,22, 24,25,26,27,28, 30,31,32,33,34],
               [0,1,2,3,4,5,    7,8,9,10,11,12, 14,15,16,17,18,19,  21,22,23,24,25,26,  28,29,30,31,32,33,  35,36,37,38,39,40,  42,43,44,45,46,47],
               [0,1,2,3,4,5,6,  8,9,10,11,12,13,14, 16,17,18,19,20,21,22,   24,25,26,27,28,29,30,   32,33,34,35,36,37,38,   40,41,42,43,44,45,46,   48,49,50,51,52,53,54,   56,57,58,59,60,61,62],
               [0,1,2,3,4,5,6,7,    9,10,11,12,13,14,15,16, 18,19,20,21,22,23,24,25,    27,28,29,30,31,32,33,34,    36,37,38,39,40,41,42,43,    45,46,47,48,49,50,51,52,    54,55,56,57,58,59,60,61,    63,64,65,66,67,68,69,70,    72,73,74,75,76,77,78,79],
               [0,1,2,3,4,5,6,7,8,
               10,11,12,13,14,15,16,17,18,
               20,21,22,23,24,25,26,27,28,
               30,31,32,33,34,35,36,37,38,
               40,41,42,43,44,45,46,47,48,
               50,51,52,53,54,55,56,57,58,
               60,61,62,63,64,65,66,67,68,
               70,71,72,73,74,75,76,77,78,
               80,81,82,83,84,85,86,87,88,
               90,91,92,93,94,95,96,97,98]]
    for index, cell in enumerate(GRIDS[level-1]):
        if index in indices[level-1]:
            if cell == door:
                print(tile.format('D'), end='')
            elif cell == monster:
                print(tile.format('M'), end='')
            elif cell == player:
                print(tile.format('X'), end='')
            else:
                print(tile.format('_'), end='')
        else:
            if cell == door:
                print(tile.format('D|'))
            elif cell == player:
                print(tile.format('X|'))
            elif cell == monster:
                print(tile.format('M|'))
            else:
                print(tile.format('_|'))


print("Welcome to the dungeon!")
print("Enter quit to exit")
print("Enter left, right, up or down to move!")

level = 1
monster, door, player = get_locations(level)

while True:
    moves = get_moves(player, level)

    print("You are currently in room {}".format(player))
    draw_map(player, level)

    move = input("> ")
    move= move.upper()
    if move == "QUIT":
        break

    if move in moves:
        player = move_player(player, move)
        monster = move_monster(monster, door, player)
    else:
        print("** Walls are hard, stop running into them! **")
        monster = move_monster(monster, door, player)
        continue
    if player == door:
        print("You escaped!!")
        level += 1
        if level == 9:
            print("\n" + "**********************")
            print("Holy shit you made it!")
            print("**********************" + "\n")
            break
        print("Entering level {}!".format(level))
        get_locations(level)
        continue

    elif player == monster:
        print("You were eating by the grue!")
        print("You dead now.")
        break
