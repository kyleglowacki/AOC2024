import aocd

def mul(a, b):
    return a * b

def findNextCmd(data, idx):
    idx1 = data.find("mul(", idx)
    idx2 = data.find("do()", idx)
    idx3 = data.find("don't()", idx)

    if idx1 == -1:
        # No more mul, so return -1
        return -1
    if idx2 == -1:
        if idx3 == -1:
            return idx1
        return min(idx1, idx3)
    if idx3 == -1:
        return min(idx1, idx2)
    return min(idx1, idx2, idx3)

raw = aocd.get_data(day=3, year=2024)

data = raw.splitlines()
#data = ['7 6 4 2 1', '1 2 7 8 9', '9 7 6 2 1']
data = ''.join(data)

ld = len(data)
idx = 0
done = False
sum = 0
while not done:
    idx = data.find("mul(", idx)
    #print(f"Next mul possibility at idx = {idx}")
    if idx == -1:
        done = True
    else:
        endIdx = data.find(")", idx)
        #print(f"Next mul possibility ends at idx = {endIdx}")
        if endIdx - idx < 12:
            try:
                #print(f"Expression = {data[idx:endIdx+1]}")
                val = eval(data[idx:endIdx+1])
                sum += val
                #print(f"Mul found = {val}, sum is now {sum}")
            except:
                #print(f"Expression was bad - {data[idx:endIdx+1]}")
                pass
        idx += 1
        
    
print("FIRST STAR")
print(f"first total = {sum}")


ld = len(data)
idx = 0
done = False
mult = True
sum2 = 0
while not done:
    idx = findNextCmd(data, idx)
    print(f"Next cmd possibility at idx = {idx}")
    if idx == -1:
        done = True
    else:
        # mul(a,b)
        if data[idx+2] == "l" and mult:
            endIdx = data.find(")", idx)
            try:
                #print(f"Expression = {data[idx:endIdx+1]}")
                val = eval(data[idx:endIdx+1])
                sum2 += val
                idx = endIdx
                #print(f"Mul found = {val}, sum is now {sum}")
            except:
                #print(f"Expression was bad - {data[idx:endIdx+1]}")
                idx += 1
                pass            
        # do()
        elif data[idx+2] == "(":
            mult = True
            idx += 1
        # don't()
        elif data[idx+2] == "n":
            mult = False
            idx += 1
        else:        
            idx += 1

print("SECOND STAR")
print(f"second total = {sum2}")
