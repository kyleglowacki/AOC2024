import aocd
import copy

def EvenDigits(val):
    sval = str(val)
    if (len(sval) % 2) == 0:
        svall = len(sval)//2
        sf = sval[:svall]
        sb = sval[svall:]
        return int(sf), int(sb), True
    return 0, 0, False

def Blink(line):
    result = []
    for item in line:
        f, b, ed = EvenDigits(item)
        if item == 0:
            result.append(1)
        elif ed:
            result.append(f)
            result.append(b)
        else:
            result.append(2024 * item)
    return result

def DickBlink(ld):
    result = {}
    for item in ld:
        f, b, ed = EvenDigits(item)
        if item == 0:
            try:
                result[1] = ld[0] + result[1]
            except KeyError:
                result[1] = ld[0]
        elif ed:
            try:
                result[f] = ld[item] + result[f]
            except KeyError:
                result[f] = ld[item]            
            try:
                result[b] = ld[item] + result[b]
            except KeyError:
                result[b] = ld[item] 
        else:
            try:
                result[2024 * item] = ld[item] + result[2024 * item]
            except KeyError:
                result[2024 * item] = ld[item]             
    return result


raw = aocd.get_data(day=11, year=2024)
data = []
rawdata = raw.splitlines()

data = rawdata[0].split(' ')
original_line = [int(x) for x in list(data)]
line = copy.deepcopy(original_line)
print(line)

print("Loaded data")

for i in range(25):
    line = Blink(line)
    print(f"{i} - {len(line)}")

print("FIRST STAR")
print(f"first total = {len(line)}")

line = copy.deepcopy(original_line)
ld = {}
for item in line:
    ld[item] = 1

for i in range(75):
    ld = DickBlink(ld)
    print(f"{i} - {len(ld)}")

sum = 0
for item in ld:
    sum += ld[item]
print("SECOND STAR")
print(f"second total = {sum}")
