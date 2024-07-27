n, x, y = (map(int, input().split()))
a = (list(map(int, input().split())))
b = (list(map(int, input().split())))

dishesA, dishesB = [], []

for i in range(n):
    dishesA.append((a[i], b[i]))
    dishesB.append((b[i], a[i]))

dishesA = sorted(dishesA)[::-1]
dishesB = sorted(dishesB)[::-1]

sw_ct, sa_ct = 0, 0

for i in range(n):
    x -= dishesA[i][0]
    y -= dishesB[i][0]
    
    if x < 0 or y < 0:
        print(i + 1)
        quit()
print(n)

