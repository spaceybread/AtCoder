import math
n = int(input())
#n, k, m = (map(int, input().split()))
#a = list(map(int, input().split()))
#b = list(map(int, input().split()))

out = []

while n > 0:
    e = math.floor(math.log(n, 3))
    n -= 3**e
    out.append(e)

print(len(out))
print(*out)
