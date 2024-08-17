n, k = map(int, input().split())
a = list(map(int, input().split()))

a = a + a

c = 0

for i in range(n):
    s = 0
    for j in range(i, n + i):
        s += a[j]
        if s % k == 0:
            c += 1

print(c)
