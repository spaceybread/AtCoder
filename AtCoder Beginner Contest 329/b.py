n = int(input())
a = input().split()

for i in range(n):
    a[i] = int(a[i])

maxN = max(a)

for i in range(n):
    if a[i] == maxN:
        a[i] = 0

print(max(a))

