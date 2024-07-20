#n = int(input())
n, t, p = (map(int, input().split()))
a = list(map(int, input().split()))
#b = list(map(int, input().split()))

l = sorted(a)[::-1]

d = (t - l[p - 1])
if d > 0:
    print(d)
else:
    print(0)



