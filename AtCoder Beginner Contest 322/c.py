lineIn = input().split()

n = int(lineIn[0])
m = int(lineIn[1])

a = input().split()

i = 1
daysTo = 0
ind = 0

while i < n + 1:
    daysTo = int(a[ind]) - i

    if daysTo == 0:
        ind = ind + 1

    print(daysTo)
    i = i + 1
