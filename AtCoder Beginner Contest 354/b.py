n = int(input())
#n, x, y, z = (map(int, input().split()))
#a = list(map(int, input().split()))
#b = list(map(int, input().split()))

s = []
c = 0

for i in range(n):
    a = input().split()
    s.append(a[0])
    c += int(a[1])

s = sorted(s)

t = c % n

print(s[t])
