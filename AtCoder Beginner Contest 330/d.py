#TLE

ln = input().split()
n = int(ln[0])
q = int(ln[1])

a = input().split()
min = 1000000000
for i in range(n):
    a[i] = int(a[i])
    if a[i] < min:
        min = a[i]

min = 0

for qi in range(q):
    qk = input().split()
    ik = int(qk[0]) - 1
    xk = int(qk[1])
    
    a[ik] = xk
    
    
    min = 0
    while True:
        if min not in a:
            break
        min = min + 1
    print(min)
    
    
    
