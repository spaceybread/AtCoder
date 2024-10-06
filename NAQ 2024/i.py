n = int(input())
#n, m = (map(int, input().split()))
#a = list(map(int, input().split()))
#b = list(map(int, input().split()))
#print(m, k, n)
valid = [[False for _ in range(n)] for _ in range(n)]

def light(x, y):
    i = 1
    valid[x][y] = True
    while x + i < n:
        if board[x + i][y] == ".":
            valid[x + i][y] = True
        elif board[x + i][y] == "?":
            return False
        else:
            break
        i+= 1
    
    i = -1
    while x + i > -1:
        if board[x + i][y] == ".":
            valid[x + i][y] = True
        elif board[x + i][y] == "?":
            return False
        else:
            break
        i-= 1
    
    i = 1
    while y + i < n:
        if board[x][y+i] == ".":
            valid[x][y + i] = True
        elif board[x][y + i] == "?":
            return False
        else:
            break
        i+= 1
    
    i = -1
    while y + i > -1:
        if board[x][y + i] == ".":
            valid[x][y + i] = True
        elif board[x][y + i] == "?":
            return False
        else:
            break
        i-= 1
    
    return True

board = []

for _ in range(n):
    board.append(list(input()))

for i in range(n):
    for j in range(n):
        if board[i][j] == "?":
            if not light(i, j):
                print(0)
                quit()
        elif board[i][j] == "X":
            valid[i][j] = True
        elif board[i][j] == ".":
            pass
        else:
            cx = int(board[i][j])
            
            if i - 1 > -1:
                if board[i - 1][j] == "?":
                    cx -= 1
            if i + 1 < n:
                if board[i + 1][j] == "?":
                    cx -= 1
            if j - 1 > -1:
                if board[i][j - 1] == "?":
                    cx -= 1
            if j + 1 < n:
                if board[i][j + 1] == "?":
                    cx -= 1
                    
            if cx == 0:
                valid[i][j] = True
        
for i in range(n):
    if False in valid[i]:
        print(0)
        quit()

print(1)
