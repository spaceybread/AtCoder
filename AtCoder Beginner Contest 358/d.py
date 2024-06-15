#n = int(input())
n, m = (map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()

idx = 0
c = 0
d = 0

for i in range(m):
    while idx < n:
        if a[idx] >= b[i]:
          c += a[idx]
          d += 1
          idx += 1
          break
        idx += 1

if d == m:
    print(c)
else:
    print(-1)

