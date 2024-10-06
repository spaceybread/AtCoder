n = int(input())
#n, k, m = (map(int, input().split()))
#a = list(map(int, input().split()))
#b = list(map(int, input().split()))
#print(m, k, n)

all = []
for i in range(n):
    x1, y1, x2, y2 = (map(int, input().split()))
    
    if (x2 >= 0 >= x1) or (x1 >= 0 >= x2):
        y = (y2 - y1) / (x2 - x1) * (-x1) + y1
        if y > 0:
            all.append(y)

if len(all) > 0:
    print(sorted(all)[0])
else:
    print(-1.0)

