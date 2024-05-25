#n = int(input())

n, t = (map(int, input().split()))
a = (list(map(int, input().split())))

sheet = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        sheet[i][j] = n * (i) + j + 1


rows = [0] * n
columns = [0] * n
lr = 0
rl = 0

sol = -1

for i in range(t):
    val = a[i]
    col = (val - 1) % n
    columns[col] += 1
    
    row = int((val - 1 - col) / n)
    rows[row] += 1
    
    if row == col:
        lr += 1
    
    if row + col == n - 1:
        rl += 1
    
    flag = False
    
    for j in rows:
        if j == n:
            flag = True
    for j in columns:
        if j == n:
            flag = True
            
    if lr == n or rl == n:
        flag = True
    
    #print(val, row, col, lr, rl)
    if sol == -1 and flag == True:
        sol = i + 1

print(sol)
