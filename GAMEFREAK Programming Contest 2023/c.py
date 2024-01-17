# editorial solution, checking out how dfs solutions work

def dfs(v, s):
    global ans
    visit[v] = True
    
    if s > ans:
        ans = s
    
    for i in range(1, n + 1):
        if not visit[i] and E[v][i]:
            dfs(i, s + E[v][i])
    visit[v] = False
    


ln = input().split()
n = int(ln[0])
m = int(ln[1])

E = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    ln = input().split()
    a = int(ln[0])
    b = int(ln[1])
    c = int(ln[2])
    
    E[a][b] = c
    E[b][a] = c

ans = 0
visit = [False]*(n + 1)

for _ in range(1, n + 1):
    dfs(_, 0)

print(ans)
