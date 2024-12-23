import aocd
import copy
import itertools

BLANK = '.'
MARK = '#'
DIRS = [[-1,0],[1,0],[0,-1],[0,1]]

def convert_string_to_int(ls):
    return list(map(int, ls))

def make_matrix(l, w, v):
    return [[v for _ in range(w)] for _ in range(l)]

def count_matrix_items(m, v):
    cnt=0
    for y, row in enumerate(m):
        for x, col in enumerate(row):
            if col == v:
                cnt += 1
    return cnt

def on_board(farm, x, y):
    if (x < 0) or (y < 0):
        return False
    if (x >= len(farm[0])) or (y >= len(farm)):
        return False
    return True

def check_location(farm, pos, value):
    if on_board(farm, pos[0], pos[1]):
        return farm[pos[1]][pos[0]] == value
    return False

def DoMoves(board, moves, value):
    nm = []
    for move in moves:
        if check_location(board, move, BLANK):
            board[move[1]][move[0]] = value
            # Now check adjacent and add to new moves
            for dir in DIRS:
                nm.append([move[0] + dir[0], move[1] + dir[1]])
    return nm


def SolveMaze(board):
    cnt = 0
    moves = [[0,0]]
    while board[70][70] == '.' and len(moves) > 0:
        moves = DoMoves(board, moves, cnt)
        cnt += 1
    return cnt, len(moves) != 0

raw = aocd.get_data(day=18, year=2024)

data = raw.splitlines()
board = make_matrix(71, 71, '.')

clean_board = copy.deepcopy(board)

print("Loaded data")

ccnt = 0
for line in data:
    if ccnt < 1024:
        corrupt = convert_string_to_int(line.split(','))
        board[corrupt[1]][corrupt[0]] = '#'
    ccnt += 1

clean_board = copy.deepcopy(board)
print("Marked data")

cnt_moves, success = SolveMaze(board)

print("FIRST STAR")
print(f"first total = {board[70][70]}")

board = copy.deepcopy(clean_board)
ccnt = 0
for line in data:
    corrupt = convert_string_to_int(line.split(','))
    board[corrupt[1]][corrupt[0]] = '#'
    if ccnt >= 1024:
        working = copy.deepcopy(board)
        cnt_moves, success = SolveMaze(working)
        print(f"{ccnt}, {cnt_moves}, {success}, {line}")
        if not success:
            print("SECOND STAR")
            print(f"second = {line}")
            exit()
    ccnt += 1

        

