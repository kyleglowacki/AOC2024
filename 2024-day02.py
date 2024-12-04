import aocd
            
def isGoodDiff(items):
    diffs = [j-i for i, j in zip(items[:-1], items[1:])]
    # Check all pos or all neg
    if len(diffs) == len([x for x in diffs if x < 0]):
        # All negative
        print(f"All negative - Convert to positive = {diffs}")
        diffs = [-x for x in diffs]

    # All positive (or negative now)
    if len(diffs) == len([x for x in diffs if x > 0]):
        print(f"All positive = {diffs}")
        if max(diffs) < 4 and min(diffs) > 0:
            print(f"Found one! = {diffs}")
            return True        
    return False

def canBeGoodDiff(items):
    if isGoodDiff(items):
        return True
    # Loop over items and drop one and see if its good.
    for idx, item in enumerate(items):
        # Build a new list
        newItems = items[:idx] + items[idx+1:]
        #import pdb;pdb.set_trace()
        if isGoodDiff(newItems):
            return True

    return False
 
raw = aocd.get_data(day=2, year=2024)

data = raw.splitlines()
#data = ['7 6 4 2 1', '1 2 7 8 9', '9 7 6 2 1']

cnt1 = 0
cnt2 = 0
for line in data:
    items = line.split(' ')
    for idx, item in enumerate(items):
        items[idx] = int(item)
   
    #import pdb;pdb.set_trace()

    if isGoodDiff(items):
        print(f"Found one! = {items}")
        cnt1 = cnt1+1
    if canBeGoodDiff(items):
        print(f"Found one! = {items}")
        cnt2 = cnt2+1

print("FIRST STAR")
print(f"first total = {cnt1}")
print("SECOND STAR")
print(f"second total = {cnt2}")