from collections import deque, defaultdict

def solve(N, M, edges):
    x = [None] * (N + 1)
    
    adj = defaultdict(list)
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, -w))
    
    def bfs(start):
        queue = deque([start])
        x[start] = 0
        
        while queue:
            u = queue.popleft()
            current_val = x[u]
            
            for v, w in adj[u]:
                if x[v] is None:
                    x[v] = current_val + w
                    queue.append(v)
                else:
                    if x[v] != current_val + w:
                        pass

    for i in range(1, N + 1):
        if x[i] is None:
            bfs(i)
    
    return x[1:]

#n = int(input())
n, m = (map(int, input().split()))
#a = list(map(int, input().split()))
e = []

for i in range(m):
    u, v, w = (map(int, input().split()))
    e.append((u, v, w))


print(*solve(n, m, e))
