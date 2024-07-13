#n = int(input())
#r, g, b = (map(int, input().split()))
#a = list(map(int, input().split()))
#b = list(map(int, input().split()))

x = [None] * 3
y = [None] * 3

for i in range(3):
    x[i], y[i] = (map(int, input().split()))


d = [None] * 3
for i in range(3):
    d[i] = (x[i] - x[(i + 1) % 3]) ** 2 + (y[i] - y[(i + 1) % 3]) ** 2

d.sort()

if d[0] + d[1] == d[2]:
    print("Yes")
else:
    print("No")

