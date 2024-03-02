# i thought i smarter than I really am and skipped to problem D, which meant that I just didn't do a really easy question for some reason

def trav(w, h, n, seq, grid):
    
    for i in range(n):
        #print(seq[i], h + 1, w +1)
        
        if seq[i] == 'L':
            if grid[h][w - 1] == "#":
                return 0
            w = w - 1
        if seq[i] == 'R':
            if grid[h][w + 1] == "#":
                return 0
            w = w + 1
        if seq[i] == 'U':
            if grid[h - 1][w] == "#":
                return 0
            h = h - 1
        if seq[i] == 'D':
            if grid[h + 1][w] == "#":
                return 0
            h = h + 1
    
    return [h, w]
    
    
    
h, w, n = (map(int, input().split()))

t = input()

grid = []

for i in range(h):
    grid.append(input())

sols = []

for w_i in range(w):
    for h_i in range(h):
        if (grid[h_i][w_i] == "."):
            #print(w_i + 1, h_i + 1)
            a = trav(w_i, h_i, n, t, grid)
            #print(a)
            if a != 0:
                sols.append(a)

print(len(sols))
