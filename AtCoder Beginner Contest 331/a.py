ln = input().split()
M = int(ln[0])
D = int(ln[1])

ln = input().split()
y = int(ln[0])
m = int(ln[1])
d = int(ln[2])


d = d + 1

if d > D:
    d = 1
    m = m + 1

if m > M:
    m = 1
    y = y + 1
    
print(y, m, d)

