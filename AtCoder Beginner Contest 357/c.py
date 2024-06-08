n = int(input())
#n, m = (map(int, input().split()))
#a = list(map(int, input().split()))
#b = list(map(int, input().split()))

def solve(n):
    if n == 0:
        return ["#"]
    
    grid = [None] * 3**n
    for i in range(3**n):
        grid[i] = [None] * 3**n

    x = 3**(n - 1)
    
    lower = solve(n - 1)
        
    for i in range(0, x):
        for j in range(0, x):
            grid[i][j] = lower[i % 3**(n - 1)][j % 3**(n - 1)]
    
    for i in range(x, 2*x):
        for j in range(0, x):
            grid[i][j] = lower[i % 3**(n - 1)][j % 3**(n - 1)]
    
    for i in range(2*x, 3*x):
        for j in range(0, x):
            grid[i][j] = lower[i % 3**(n - 1)][j % 3**(n - 1)]
    
    for i in range(0, x):
        for j in range(x, 2*x):
            grid[i][j] = lower[i % 3**(n - 1)][j % 3**(n - 1)]
    
    for i in range(2*x, 3*x):
        for j in range(x, 2*x):
            grid[i][j] = lower[i % 3**(n - 1)][j % 3**(n - 1)]

    for i in range(0, x):
        for j in range(2*x, 3*x):
            grid[i][j] = lower[i % 3**(n - 1)][j % 3**(n - 1)]
    
    for i in range(x, 2*x):
        for j in range(2*x, 3*x):
            grid[i][j] = lower[i % 3**(n - 1)][j % 3**(n - 1)]
    
    for i in range(2*x, 3*x):
        for j in range(2*x, 3*x):
            grid[i][j] = lower[i % 3**(n - 1)][j % 3**(n - 1)]
    
    for i in range(x, 2*x):
        for j in range(x, 2*x):
            grid[i][j] = "."
    
    
    
    
    
    return grid
    
b = solve(n)

for l in b:
    print("".join(l))
