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

def IsPossible(pat, avail, fails):
    # Can we build p from the items in a?
    if len(pat) == 0:
        return True, fails
    
    for a in avail:
        if pat.startswith(a):
            if pat[len(a):] not in fails:
                #print(f"Using {a} and now working {pat}")
                possible, fails = IsPossible(pat[len(a):], avail, fails)
                if possible:
                    return True, fails
                else:
                    fails.append(pat[len(a):])
    return False, fails

def CountPossible(pat, avail, sucks):
    pcount = 0
    # Can we build p from the items in a?
    if len(pat) == 0:
        print("ERROR")
        exit()
    # Find possible starters
    starters = []
    for a in avail:
        if pat.startswith(a) and len(a) <= len(pat):
            starters.append(a)
            
    #print(f"Working on {pat} - {starters}")
    for start in starters:
        #print(f"Considering {start} from {starters} on {pat}")
        if len(start) == len(pat):
            #print(f"Perfect Fit - Increment count   {len(start)} {len(pat)} {start} {pat}")
            pcount += 1
        elif pat[len(start):] in sucks:
            # We know this count already
            #print(f"We already know {pat[len(start):]} is {sucks[pat[len(start):]]}")
            pcount += sucks[pat[len(start):]]
        else:
            # We don't know this count yet
            #print(f"Using {start} and now working {pat[len(start):]}, count = {pcount}")
            subcount, sucks = CountPossible(pat[len(start):], avail, sucks)
            if subcount > 0:
                #print(f"  {pat[len(start):]} returned count = {subcount}")
                sucks[pat[len(start):]] = subcount
            pcount += subcount

    #print(f"Finished  on {pat} = {pcount}")
    return pcount, sucks


raw = aocd.get_data(day=19, year=2024)

data = raw.splitlines()
#data = ["a,b,c,d,bc,ab,abc","","abcd"]
#data = ["bwg,bw,b,br,brb,rb,r,g,gbr,wgb,wg,wgbr","","bwgbrb"]

avail = data[0].split(',')
for idx, a in enumerate(avail):
    avail[idx] = a.strip()
patterns = data[2:]
print("Loaded data")

#print(avail)

towels = []

cnt = 0
for pattern in patterns:
    #import pdb;pdb.set_trace()
    possible, fails = IsPossible(pattern, avail, [])
    if possible:
        #print(f"Figured out {pattern}")
        cnt += 1
        towels.append(pattern)
    #else:
    #    print(f"{pattern}  NOT POSSIBLE")
print("FIRST STAR")
print(f"first total = {cnt}")

# Work on towels to show all possible ways
pc = 0
sum = 0
#towels = ["wrwubwgbbwgrrrugwwruburrrbwgrrruwwbggrbugbbwgbrb"]
#towels = ['bwgbrb']
sucks = {}
for towel in towels:
    print(f"Starting {towel}")
    pc, fails = CountPossible(towel, avail, sucks)
    #print(sucks)
    sum += pc
    print(f"Counted {towel} has {pc}, now sum is {sum}")

print("SECOND STAR")
print(f"second = {sum}")
