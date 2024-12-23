import aocd
import copy
import heapq

MARK = '#'
#         W      N      E     S
DIRS = [[-1,0],[0,-1],[1,0],[0,1]]

def make_matrix(l, w, v):
    return [[v for _ in range(w)] for _ in range(l)]

def count_matrix_items(m, v):
    cnt=0
    for y, row in enumerate(m):
        for x, col in enumerate(row):
            if col == v:
                cnt += 1
    return cnt


def compute_lowest_score(data):
    # Directions and their corresponding rotation costs
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # East, South, West, North
    rotation_cost = 1000
    move_cost = 1
    
    # Find starting and ending positions
    start = end = None
    for y, row in enumerate(data):
        for x, cell in enumerate(row):
            if cell == 'S':
                start = (x, y)
            elif cell == 'E':
                end = (x, y)
    
    if not start or not end:
        raise ValueError("Start or End position not found in the data")
    
    # Priority queue for A* search
    pq = []
    # Initial state: position, direction (0 for East), and score
    heapq.heappush(pq, (0, start, 0))  # (score, position, direction_index)
    
    # Visited dictionary to store the minimum cost to reach each cell with each direction
    visited = {}
    
    while pq:
        score, (x, y), direction = heapq.heappop(pq)
        
        if (x, y) == end:
            print(f"Reached end: score={score}, position=({x}, {y}), direction={direction}")
            return score
        
        if (x, y, direction) in visited and visited[(x, y, direction)] <= score:
            continue
        
        visited[(x, y, direction)] = score
        
        # Move forward in the current direction
        dx, dy = directions[direction]
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(data[0]) and 0 <= ny < len(data) and data[ny][nx] != '#':
            heapq.heappush(pq, (score + move_cost, (nx, ny), direction))
        
        # Rotate clockwise and counterclockwise
        for new_direction in [(direction + 1) % 4, (direction - 1) % 4]:
            if (x, y, new_direction) not in visited or visited[(x, y, new_direction)] > score + rotation_cost:
                heapq.heappush(pq, (score + rotation_cost, (x, y), new_direction))
    
    return float('inf')  # If no path is found

raw = aocd.get_data(day=16, year=2024)
data = raw.splitlines()
'''
data = [
    "###############",
    "#.......#....E#",
    "#.#.###.#.###.#",
    "#.....#.#...#.#",
    "#.###.#####.#.#",
    "#.#.#.......#.#",
    "#.#.#####.###.#",
    "#...........#.#",
    "###.#.#####.#.#",
    "#...#.....#.#.#",
    "#.#.#.###.#.#.#",
    "#.....#...#.#.#",
    "#.###.#.#.#.#.#",
    "#S..#.....#...#",
    "###############"
]

data = [
"#################",
"#...#...#...#..E#",
"#.#.#.#.#.#.#.#.#",
"#.#.#.#...#...#.#",
"#.#.#.#.###.#.#.#",
"#...#.#.#.....#.#",
"#.#.#.#.#.#####.#",
"#.#...#.#.#.....#",
"#.#.#####.#.###.#",
"#.#.#.......#...#",
"#.#.###.#####.###",
"#.#.#...#.....#.#",
"#.#.#.#####.###.#",
"#.#.#.........#.#",
"#.#.#.#########.#",
"#S#.............#",
"#################"
    ]
'''
data = [list(row) for row in data]
score = compute_lowest_score(data)


print("FIRST STAR")
print(f"first total = {score}")
from collections import deque

def find_best_paths(data):
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # East, South, West, North
    rotation_cost = 1000
    move_cost = 1
    
    start = end = None
    for y, row in enumerate(data):
        for x, cell in enumerate(row):
            if cell == 'S':
                start = (x, y)
            elif cell == 'E':
                end = (x, y)
    
    if not start or not end:
        raise ValueError("Start or End position not found in the data")
    
    pq = []
    heapq.heappush(pq, (0, start, 0))
    
    visited = {}
    min_score = None
    
    while pq:
        score, (x, y), direction = heapq.heappop(pq)
        
        if (x, y) == end:
            if min_score is None:
                min_score = score
            elif score > min_score:
                break
        
        if (x, y, direction) in visited and visited[(x, y, direction)] <= score:
            continue
        
        visited[(x, y, direction)] = score
        
        dx, dy = directions[direction]
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(data[0]) and 0 <= ny < len(data) and data[ny][nx] != '#':
            heapq.heappush(pq, (score + move_cost, (nx, ny), direction))
        
        for new_direction in [(direction + 1) % 4, (direction - 1) % 4]:
            if (x, y, new_direction) not in visited or visited[(x, y, new_direction)] > score + rotation_cost:
                heapq.heappush(pq, (score + rotation_cost, (x, y), new_direction))
    
    best_tiles = set()
    queue = deque([(end, min_score)])
    
    while queue:
        (x, y), score = queue.popleft()
        
        if (x, y) == start:
            best_tiles.add((x, y))
            continue
        
        for direction, (dx, dy) in enumerate(directions):
            nx, ny = x - dx, y - dy
            if 0 <= nx < len(data[0]) and 0 <= ny < len(data) and data[ny][nx] != '#':
                if (nx, ny, direction) in visited and visited[(nx, ny, direction)] + move_cost == score:
                    best_tiles.add((nx, ny))
                    queue.append(((nx, ny), score - move_cost))
        
        for direction, (dx, dy) in enumerate(directions):
            if (x, y, direction) in visited and visited[(x, y, direction)] + rotation_cost == score:
                best_tiles.add((x, y))
                queue.append(((x, y), score - rotation_cost))
    
    best_tiles.add(start)
    best_tiles.add(end)
    
    return best_tiles

best_tiles = find_best_paths(data)
print(best_tiles)
print("SECOND STAR")
print(f"second total = {len(best_tiles)}")
