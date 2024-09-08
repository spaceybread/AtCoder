n = int(input())
#n, k = (map(int, input().split()))
#
#b = list(map(int, input().split()))

mat = [None] * n

for i in range(n):
    a = list(map(int, input().split()))
    mat[i] = a

el = mat[0][0]

for x in range(1, n):
    el -= 1
    
    if el >= x:
        el = mat[el][x]
    else:
        el = mat[x][el]

print(el)
