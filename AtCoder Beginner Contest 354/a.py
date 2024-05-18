n = int(input())
#n, x, y, z = (map(int, input().split()))
#a = list(map(int, input().split()))
#b = list(map(int, input().split()))

i = 0
h = 0
while h < n:
    i += 1
    h += 2**i

print(i+ 1)
