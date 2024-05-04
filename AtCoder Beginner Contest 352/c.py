n = int(input())
#n, x, y, z = (map(int, input().split()))
#a = list(map(int, input().split()))
#b = list(map(int, input().split()))

sh = 0
maxdiff = -1

for i in range(n):
    a, b = (map(int, input().split()))
    
    if b - a > maxdiff:
        maxdiff = b - a
    
    sh += a

print(sh + maxdiff)
