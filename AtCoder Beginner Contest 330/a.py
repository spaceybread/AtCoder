ln = input().split()
n = int(ln[0])
l = int(ln[1])

aN = input().split()
c = 0

for i in range(n):
    if int(aN[i]) >= l:
        c = c + 1

print(c)


