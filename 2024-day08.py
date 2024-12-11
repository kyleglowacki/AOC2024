import aocd
import copy
import itertools
    

def make_matrix(l, w, v):
    return [[v for _ in range(w)] for _ in range(l)]

def MarkAntiNode(a, x, y):
    if (y < 0) or (x < 0):
        #print("Node off map")
        return a
    if (x >= len(a[0])) or (y >= len(a)):
        #print("Node off map")
        return a
    if a[y][x] == '#':
        print("Overlapping Node")
    a[y][x] = '#'
    return a

def DoCombos(a, c):
    for item in c:
        dx = item[0][0] - item[1][0]
        dy = item[0][1] - item[1][1]
        if (dx == 0) and (dy == 0):
            print("Skipping node and itself")
        else:
            for i in range(51):
                MarkAntiNode(a, item[0][0]+(dx*i), item[0][1]+(dy*i))
                MarkAntiNode(a, item[1][0]-(dx*i), item[1][1]-(dy*i))
    return a

def CountAnti(a):
    cnt=0
    for y, row in enumerate(a):
        for x, col in enumerate(row):
            if col != '.':
                cnt += 1
    return cnt

raw = aocd.get_data(day=8, year=2024)

data = raw.splitlines()

'''
data = ["............",
        "........0...",
        ".....0......",
        ".......0....",
        "....0.......",
        "......A.....",
        "............",
        "............",
        "........A...",
        ".........A..",
        "............",
        "............"]
'''
print("Loaded data")
#print(data)

# Find all letters
ants = {}
for y, row in enumerate(data):
    for x, col in enumerate(row):
        if col != '.':
            try:
                poss = ants[col]
            except KeyError:
                poss = []
            poss.append([x,y])
            ants[col] = poss
            
print("Found antenna")

# Loop over keys
ans = make_matrix(len(data), len(data[0]), '.')
for a in ants:
    print(f"Working on {a}")
    combos = list(itertools.product(ants[a], ants[a]))
    ans = DoCombos(ans, combos)
    print(f"Nodes = {CountAnti(ans)}")

a = CountAnti(ans)
print("FIRST STAR")
print(f"first total = {a}")
#print(ans)

        
print("SECOND STAR")
print(f"second total = {a}")
