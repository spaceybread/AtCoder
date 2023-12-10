ln = input().split()
n = int(ln[0])
s = int(ln[1])
k = int(ln[2])

total = 0

for _ in range(n):
    ln = input().split()
    p = int(ln[0])
    q = int(ln[1])
    
    total = total + (p * q)

if total >= s:
    print(total)
else:
    print(total + k)
