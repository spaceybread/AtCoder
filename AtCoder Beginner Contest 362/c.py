n = int(input())
#r, g, b = (map(int, input().split()))
#a = list(map(int, input().split()))
#b = list(map(int, input().split()))

l = [None] * n
r = [None] * n
lsum, rsum = 0, 0


for i in range(n):
    l[i], r[i] = (map(int, input().split()))
    lsum += l[i]
    rsum += r[i]

if not lsum <= 0 <= rsum:
    print("No")
    quit()
else:
    csum = lsum
    X = l[:]
    
    for i in range(n):
        if csum == 0:
            break
        
        delt = r[i] - l[i]
        
        if csum + delt <= 0:
           X[i] += delt
           csum += delt
        else:
           X[i] -= csum
           csum = 0

print("Yes")
print(*X)
