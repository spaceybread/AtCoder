#not mine, all correct

ln = input().split()
n = int(ln[0])
q = int(ln[1])

dragon = [(i, 0) for i in range(n, 0, -1)]
x, y = 1, 0

for _ in range(q):
    quer = input().split()
    if quer[0] == "1":
        if quer[1] == "R":
            x = x + 1
        if quer[1] == "L":
            x = x - 1
        if quer[1] == "U":
            y = y + 1
        if quer[1] == "D":
            y = y - 1
        dragon.append((x, y))
    else:
        print(*dragon[-int(quer[1])])
        
        
