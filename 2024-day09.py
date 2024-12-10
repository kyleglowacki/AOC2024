import aocd

def FindNextFileBlock(dm, back, front):

    found = False
    while not found:
        back = back -1
        if back <= front:
            #print("Some kind of logic fail... moved too far")
            found = True
        elif dm[back] != '.':
            return back, dm[back]
    raise KeyError("Index out of range")

def ComputeBlankSize(dm2, i, fIdx):
    sz = 0
    #print(f"CBS {i} {fIdx}")
    while (i < fIdx) and dm2[i] == '.':
        sz += 1
        i += 1
    return sz

def MoveFile(dm2, i, fIdx, fLen, fId):
    for idx in range(fLen):
        dm2[i + idx] = fId
        dm2[fIdx + idx] = '.'
    #print(f"Moved file {fId} of length {fLen} from {fIdx} to {i}")
    return dm2

raw = aocd.get_data(day=9, year=2024)

data = raw.splitlines()
data = data[0]
print("Loaded data")

dm = []
files = []
isFile = True
fileNumber = 0
for digit in data:
    if isFile:
        # Save off starting list of files and locations
        files.append([fileNumber, len(dm), int(digit)])
        for i in range(int(digit)):
            dm.append(fileNumber)
        fileNumber += 1
        isFile = False
    else:
        for i in range(int(digit)):
            dm.append('.')
        isFile = True

print("Processed Data")

# Make a clean copy for part 2
dm2 = dm.copy()

# Compact it
front = 0
back = len(dm)

while front < back:
    if dm[front] == '.':
        # Found a blank, move a block
        try:
            back, val = FindNextFileBlock(dm, back, front)
            #print(f"Move a {val} from {back} to {front}")
            dm[front] = val
            dm[back] = "."
        except KeyError:
            pass        
    front += 1


# Compute checksum
#print(dm)
check = 0
for idx, fileId in enumerate(dm):
    if fileId != '.':
        check += idx * fileId

print("FIRST STAR")
print(f"first total = {check}")

# Move files as a block
files.reverse()

for fd in files:
    fId = fd[0]
    fIdx = fd[1]
    fLen = fd[2]
    # Look for somewhere to put it.
    i = 0
    moved = False
    while (i < fIdx) and not moved:
        blankSize = ComputeBlankSize(dm2, i, fIdx)
        #print(f"Blanksize {blankSize} at {i}")
        if blankSize >= fLen:
            print(f"Moving {fd} to blank at {i} of size {blankSize}")
            dm2 = MoveFile(dm2, i, fIdx, fLen, fId)
            moved = True
        i += 1
    if not moved:
        print(f"Unable to move {fd}")

#Compute checksum
check2 = 0
for idx, fileId in enumerate(dm2):
    if fileId != '.':
        check2 += idx * fileId
        
print("SECOND STAR")
print(f"second total = {check2}")
