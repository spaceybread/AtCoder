#n = int(input())
n, m = (map(int, input().split()))
a = list(map(int, input().split()))
#b = list(map(int, input().split()))

t = 0

for i in range(n):
    if a[i] < t:
        t += m
        print(t)
    else:
        t = a[i] + m
        print(t)

