ln = input().split()
n = int(ln[0])
l = int(ln[1])

a = []

for i in range(n):
    a.append(input())

a.sort()

print("".join(a))
