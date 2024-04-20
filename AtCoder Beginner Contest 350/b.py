#n = int(input())
n, q = (map(int, input().split()))
t = list(map(int, input().split()))

teeth = [1] * n

c = n
for ti in t:
    if teeth[ti - 1] == 1:
        teeth[ti - 1] = 0
        c += -1
    else:
        teeth[ti - 1] = 1
        c += 1

print(c)
