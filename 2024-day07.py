import aocd

def ComputePossibilities(rest):
    #print(f"CP = {rest}")
    if len(rest) == 1:
        return rest
    head1 = rest[0] * rest[1]
    head2 = rest[0] + rest[1]
    # Remove head3 to get back to part 1
    head3 = int(str(rest[0]) + str(rest[1]))
    #import pdb;pdb.set_trace()
    return ComputePossibilities([head1] + rest[2:]) + ComputePossibilities([head2] + rest[2:]) + ComputePossibilities([head3] + rest[2:])

def ValidProblem(prob):
    print(prob)
    ans = ComputePossibilities(prob[1])
    #print(ans)
    return prob[0] in ans

raw = aocd.get_data(day=7, year=2024)

rawdata = raw.splitlines()
data = []
for line in rawdata:
    #print(line)
    ans, rest = line.split(':')
    rest = rest.strip()
    rest = rest.split(' ')
    rest = [int(x) for x in rest]
    data.append([int(ans), rest])

print("Loaded data")
#print(data)

sum = 0
for problem in data:
    print(f"P=problem, Sum={sum}")
    if ValidProblem(problem):
        sum += problem[0]

print("FIRST STAR")
print(f"first total = {sum}")

cnt = 0        
print("SECOND STAR")
print(f"second total = {cnt}")
