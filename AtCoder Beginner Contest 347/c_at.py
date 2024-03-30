n, a, b = map(int, input().split())
d = list(map(int, input().split()))

flag = True
for i in range(n):
    if d[i] % (a + b) > a:
        flag = False

if flag:
    print("Yes")
else:
    print("No")
