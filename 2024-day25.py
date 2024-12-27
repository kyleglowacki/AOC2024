import aocd
import copy
import itertools
import math

BLANK = '.'
MARK = '#'


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

def dist(pos):
    return math.sqrt(pos[0] * pos[0] + pos[1] * pos[1])


def parse_schematics(schematics):
    locks = []
    keys = []

    for schematic in schematics:
        if schematic[0][0] == '#':
            # This is a lock
            lock = [0] * len(schematic[0])
            for i in range(1, len(schematic)):
                for j in range(len(schematic[i])):
                    if schematic[i][j] == '#':
                        lock[j] += 1
            print(f"LOCK = {lock}")
            locks.append(lock)
        else:
            # This is a key
            key = [0] * len(schematic[0])
            for row in range(0,len(schematic)-1):
                for col in range(len(schematic[0])):
                    if schematic[row][col] == '#':
                        key[col] += 1
            print(f"Key = {key}")
            keys.append(key)

    return locks, keys

def count_fitting_pairs(locks, keys, height):
    fitting_pairs = 0
    for lock in locks:
        for key in keys:
            fits = True
            for l, k in zip(lock, key):
                #print(f" Test {lock} and {key} ... pin {l} + {k} >= {height}")
                if l + k >= height:
                    fits = False
                    break
            if fits:
                #print(f"FITS!  {lock} and {key}")
                fitting_pairs += 1
    return fitting_pairs


def break_up_schematics(input_list):
    schematics = []
    i = 0
    while i < len(input_list):
        if i % 8 == 7:
            # Skip the white space row
            i += 1
        else:
            # Collect the next 7 rows into a new list
            schematics.append(input_list[i:i+7])
            i += 7
    return schematics


raw = aocd.get_data(day=25, year=2024)
data = raw.splitlines()

schematics = break_up_schematics(data)


# Example input
schematics_ex = [
    [
        "#####",
        ".####",
        ".####",
        ".####",
        ".#.#.",
        ".#...",
        "....."
    ],
    [
        "#####",
        "##.##",
        ".#.##",
        "...##",
        "...#.",
        "...#.",
        "....."
    ],
    [
        ".....",
        "#....",
        "#....",
        "#...#",
        "#.#.#",
        "#.###",
        "#####"
    ],
    [
        ".....",
        ".....",
        "#.#..",
        "###..",
        "###.#",
        "###.#",
        "#####"
    ],
    [
        ".....",
        ".....",
        ".....",
        "#....",
        "#.#..",
        "#.#.#",
        "#####"
    ]
]

data = schematics
print("Loaded data")

locks, keys = parse_schematics(data)
result = count_fitting_pairs(locks, keys, len(data[0])-1)
print(result)  # Output the number of unique lock/key pairs that fit together

print("FIRST STAR")
print(f"first total = {result}")



print("SECOND STAR")
print(f"second = {result}")



