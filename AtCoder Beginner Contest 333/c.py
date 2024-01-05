all = []

a = 1
b = 1
c = 1

for i in range(12):
    b = 1
    c = 1
    for j in range(12):
        c = 1
        for k in range(12):
            if (a + b + c) not in all:
                all.append(a + b + c)
            c = c*10 + 1
        b = b*10 + 1
    a = a*10 + 1

all.sort()
#print(all)
#print(len(all))

n = int(input()) - 1
print(all[n])

