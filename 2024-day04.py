import aocd


def check(data, x, y, dirs, lets):

    num = 0

    for dir in dirs:
        valid = True
        for idx, let in enumerate(lets):
            if data[x + dir[idx][0]][y + dir[idx][1]] != let:
                valid = False
        if valid:
            print(f"Found one - {dir} at {x-3},{y-3}")
            num += 1
        #else:
        #   print(f"Not found - {dir} at {x-3},{y-3}")
    return num
    

raw = aocd.get_data(day=4, year=2024)

rawlines = raw.splitlines()

#rawlines = ["MMMSXXMASM","MSAMXMSMSA","AMXSXMAAMM","MSAMASMSMX","XMASAMXAMM","XXAMMXXAMA","SMSMSASXSS","SAXAMASAAA","MAMMMXMMMM","MXMXAXMASX"]

rawlen = len(rawlines)
finlen = len(rawlines[0]) + 6
data = [ [] for _ in range(rawlen + 6)]
data[0] = "." * finlen
data[1] = "." * finlen
data[2] = "." * finlen
data[-1] = "." * finlen
data[-2] = "." * finlen
data[-3] = "." * finlen
for idx, line in enumerate(rawlines):
    data[idx+3] = "..." + line + "..."



idx = 0
done = False
cnt = 0

dirs = [[[ 1, 0],[ 2, 0],[ 3, 0]],
        [[ 1, 1],[ 2, 2],[ 3, 3]],
        [[ 0, 1],[ 0, 2],[ 0, 3]],
        [[-1, 1],[-2, 2],[-3, 3]],
        [[-1, 0],[-2, 0],[-3, 0]],
        [[-1,-1],[-2,-2],[-3,-3]],
        [[ 0,-1],[ 0,-2],[ 0,-3]],
        [[ 1,-1],[ 2,-2],[ 3,-3]]]
lets = ["M", "A", "S"]


for row in range(len(data)):
    for col in range(len(data[0])):
        if data[row][col] == "X":
            cnt += check(data, row, col, dirs, lets)
        
    
print("FIRST STAR")
print(f"first total = {cnt}")

# Based on the A, where are the M and S and M and S
dirs = [#[[ 1, 0],[-1, 0],[ 0, 1],[ 0,-1]],
        #[[ 1, 0],[-1, 0],[ 0,-1],[ 0, 1]],  NOT +, only X
        #[[-1, 0],[ 1, 0],[ 0, 1],[ 0,-1]],
        #[[-1, 0],[ 1, 0],[ 0,-1],[ 0, 1]],
        [[ 1, 1],[-1,-1],[-1, 1],[ 1,-1]],
        [[ 1, 1],[-1,-1],[ 1,-1],[-1, 1]],
        [[-1,-1],[ 1, 1],[-1, 1],[ 1,-1]],
        [[-1,-1],[ 1, 1],[ 1,-1],[-1, 1]]]

lets = ["M", "S", "M", "S"]

cnt2 = 0
for row in range(len(data)):
    for col in range(len(data[0])):
        if data[row][col] == "A":
            cnt2 += check(data, row, col, dirs, lets)

print("SECOND STAR")
print(f"second total = {cnt2}")
