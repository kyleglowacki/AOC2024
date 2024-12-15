import aocd
import copy

MARK = '#'
DIRS = [[-1,0],[1,0],[0,-1],[0,1]]

def make_matrix(l, w, v):
    return [[v for _ in range(w)] for _ in range(l)]

def count_matrix_items(m, v):
    cnt=0
    for y, row in enumerate(m):
        for x, col in enumerate(row):
            if col == v:
                cnt += 1
    return cnt

def ComputeButtonPresses(claw, bLimit):
    aCnt = 0
    bCnt = 0
    '''
    Button A: X+94, Y+34
    Button B: X+22, Y+67
    Prize: X=8400, Y=5400
    '''

    # use det
    # y = (a*f-c*d) / (a*e-b*d)
    # y = (AX*CONDY - CONDX * AY) / (AX*BY-BX*AY)
    det = (claw["A-X"] * claw["B-Y"]) - (claw["B-X"] * claw["A-Y"])
    # Solve for A /B
    aCnt = ((claw["COND-X"] * claw["B-Y"]) - (claw["COND-Y"] * claw["B-X"])) / det
    bCnt = ((claw["A-X"] * claw["COND-Y"]) - (claw["COND-X"] * claw["A-Y"])) / det


    if (not aCnt.is_integer()) or (not bCnt.is_integer()):
        print(f"Unable to compute {aCnt} {bCnt} from {claw}")
        raise ValueError
    if (aCnt > bLimit) or (bCnt > bLimit):
        print(f"Answer too large {aCnt} {bCnt} from {claw}")
        raise ValueError

    return int(aCnt), int(bCnt)


raw = aocd.get_data(day=13, year=2024)

data = raw.splitlines()
data2 = ["Button A: X+94, Y+34",
"Button B: X+22, Y+67",
"Prize: X=8400, Y=5400",
"",
"Button A: X+26, Y+66",
"Button B: X+67, Y+21",
"Prize: X=12748, Y=12176",
"",
"Button A: X+17, Y+86",
"Button B: X+84, Y+37",
"Prize: X=7870, Y=6450",
"",
"Button A: X+69, Y+23",
"Button B: X+27, Y+71",
"Prize: X=18641, Y=10279"]


tmp = copy.deepcopy(data)
trips = []
aa = ""
bb = ""
pp = ""
while len(tmp) > 0:
    line = tmp[0]
    if "Button A" in line:
        aa = line
    if "Button B" in line:
        bb = line
    if "Prize" in line:
        pp = line
        trips.append([aa,bb,pp])
    tmp = tmp[1:]

qs = []
for trip in trips:
    q = {}
    q["A-X"] = int(trip[0].split(":")[1].strip().split(',')[0].split('+')[1])
    q["A-Y"] = int(trip[0].split(":")[1].strip().split(',')[1].split('+')[1])
    q["B-X"] = int(trip[1].split(":")[1].strip().split(',')[0].split('+')[1])
    q["B-Y"] = int(trip[1].split(":")[1].strip().split(',')[1].split('+')[1])
    q["COND-X"] = int(trip[2].split(':')[1].split(',')[0].split('=')[1].strip())
    q["COND-Y"] = int(trip[2].split(':')[1].split(',')[1].split('=')[1].strip())
    qs.append(q)

#print(qs)
tokens = 0
for q in qs:
    try:
        a,b = ComputeButtonPresses(q, 100.0)
        print(f"COMPUTE {a},{b}")
        cost = (a * 3) + b
        tokens += cost
    except ValueError:
        pass

# 28753 (right)
print("FIRST STAR")
print(f"first total = {tokens}")

tokens = 0
for q in qs:
    try:
        q["COND-X"] = 10000000000000 + q["COND-X"]
        q["COND-Y"] = 10000000000000 + q["COND-Y"]
        a,b = ComputeButtonPresses(q, 1000000000000000.0)
        print(f"COMPUTE {a},{b}")
        cost = (a * 3) + b
        tokens += cost
    except ValueError:
        pass
        
print("SECOND STAR")
print(f"second total = {tokens}")
