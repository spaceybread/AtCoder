#n, t = map(int, input().split())

a = [-1]

while a[-1] != 0:
    a.append(int(input()))

a = a[::-1]

N = len(a)

for i in range(0, N - 1):
    print(a[i])

