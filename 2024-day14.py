import aocd
import copy
    
def make_matrix(l, w, v):
    return [[v for _ in range(w)] for _ in range(l)]

def MoveRobots(h, robots, t):
    newRobots = []
    for r in robots:
        # Just move
        newr1 = [r[0] + r[2] * t, r[1] + r[3] * t, r[2], r[3]]
        # Clip to hall
        newr2 = [newr1[0] % len(h[0]), newr1[1] % len(h), newr1[2], newr1[3]]
        newRobots.append(newr2)
    return newRobots

def CountQuads(robots, minX, maxX, minY, maxY):
    cnt = 0
    for r in robots:
        if r[0] >= minX and r[0] <= maxX:
            if r[1] >= minY and r[1] <= maxY:
                cnt += 1
    return cnt

def CountRowGT(hall, robots, cnt):
    sums = []
    for h in hall:
        sums.append(0)
    for r in robots:
        sums[r[1]] += 1
    ans = 0
    for sum in sums:
        if sum > cnt:
            ans += 1
    return ans

def print_hall(hall, robots):
    hh = copy.deepcopy(hall)
    for r in robots:
        hh[r[1]][r[0]] = '#'
    ss = f"{hh}"
    ss = ss.replace(" ' ',"," ")
    ss = ss.replace(" '#',","#")
    print(ss)

raw = aocd.get_data(day=14, year=2024)
data = raw.splitlines()
hall = make_matrix(103, 101, ' ')
'''
data = ["p=0,4 v=3,-3",
        "p=6,3 v=-1,-3",
        "p=10,3 v=-1,2",
        "p=2,0 v=2,-1",
        "p=0,0 v=1,3",
        "p=3,0 v=-2,-2",
        "p=7,6 v=-1,-3",
        "p=3,0 v=-1,-2",
        "p=9,3 v=2,3",
        "p=7,3 v=-1,2",
        "p=2,4 v=2,-3",
        "p=9,5 v=-3,-3"]
hall = make_matrix(7, 11, ' ')
'''

robots = []
for robot in data:
    pos, vel = robot.split(' ')
    pos = pos.split('=')[1]
    pos = pos.split(',')
    vel = vel.split('=')[1]
    vel = vel.split(',')
    robots.append([int(pos[0]), int(pos[1]), int(vel[0]), int(vel[1])])
robotsp2 = copy.deepcopy(robots)


# Move Robots 100 steps in the hall
robots = MoveRobots(hall, robots, 100)
#X 0-49, 50, 51-100
#Y 0-50, 51, 52-102
quads = [CountQuads(robots, 0, 49, 0, 50), CountQuads(robots, 0, 49, 52, 102), CountQuads(robots, 51, 100, 0, 50), CountQuads(robots, 51, 100, 52, 102)]
#X 0-4, 5, 6-10
#Y 0-2, 3, 4-6
#quads = [CountQuads(robots, 0, 4, 0, 2), CountQuads(robots, 0, 4, 4, 6), CountQuads(robots, 6, 10, 0, 2), CountQuads(robots, 6, 10, 4, 6)]
print(quads)

print("******************* FIRST STAR ***************")
total = 1
for q in quads:
    total *= q
print(f"FIRST total = {total}")
# 204528870 Too low

print("********** SECOND STAR *************")
total2 = 0
robots = robotsp2
done = False
cnt = 0
while not done:
    robots = MoveRobots(hall, robots, 1)
    cnt += 1
    if (cnt > 101*103):
        print(f"FAIL")
        exit()
    # Count how many rows have more than 20 robots
    if CountRowGT(hall, robots, 10) > 8:
        print(cnt)
        print_hall(hall, robots)
        

print(f"SECOND total = {total2}")
