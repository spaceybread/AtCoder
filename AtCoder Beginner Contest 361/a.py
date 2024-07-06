#n = int(input())
n, k, x = (map(int, input().split()))
a = list(map(int, input().split()))
#b = list(map(int, input().split()))

b = []

for i in range(n + 1):
    if i < k:
        b.append(str(a[i]))
    elif i == k:
        b.append(str(x))
    else:
        b.append(str(a[i - 1]))

print(" ".join(b))

