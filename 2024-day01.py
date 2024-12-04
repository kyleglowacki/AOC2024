import aocd
            
                        
        
raw = aocd.get_data(day=1, year=2024)

data = raw.splitlines()
# ['3   4','4   3' .. ]

first = []
second = []

for line in data:
    items = line.split(' ')
    f = int(items[0])
    s = int(items[-1])
    first.append(f)
    second.append(s)

# Sort
first.sort()
second.sort()

print("FIRST STAR")
ds = 0
for idx, item in enumerate(first):
    #import pdb;pdb.set_trace()
    diff = abs(first[idx] - second[idx])
    ds += diff

print(f"first total = {ds}")

ss = 0
print("SECOND STAR")
for idx, item in enumerate(first):
    #import pdb;pdb.set_trace()
    sim = second.count(first[idx]) * first[idx]
    ss += sim

print(f"second total = {ss}")