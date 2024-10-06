n = int(input())
#n, k, m = (map(int, input().split()))
#a = list(map(int, input().split()))
#b = list(map(int, input().split()))
#print(m, k, n)

c = 0
for _ in range(n):
    d = int(input())
    if d % 2 == 1: c += 1

print(c)
