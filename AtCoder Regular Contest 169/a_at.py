#WA

n = int(input())
a = input().split()
p = input().split()

for i in range(n):
    a[i] = int(a[i])

for i in range(n - 1):
    p[i] = int(p[i])

#print(a, p)

for _ in range(110):
    for i in range(1, n):
        a[p[i - 1] - 1] = a[i] + a[p[i - 1] - 1]

su = 0
for s in a:
    su = su + s
#print(su)

if su == 0:
    print(0)
elif su >= a[0]:
    if su < 0:
        print('-')
    else:
        print('+')
elif su <= -1*a[0]:
    print('-')
else:
    print(0)

#print(a[0])
