n = int(input())
#r, g = (map(int, input().split()))
a = (list(map(int, input().split())))
#b = list(map(int, input().split()))

d = {}

for i in range(n):
    d[a[i]] = i

a = sorted(a)

a.pop(-1)
print(d[a.pop(-1)] + 1)
