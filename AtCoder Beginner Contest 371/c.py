import itertools

def calc(perm, adj_G, adj_H, A, N):
    total_cost = 0
    for i in range(N):
        for j in range(i + 1, N):
            u, v = perm[i], perm[j]
            g_edge = adj_G[i][j]
            h_edge = adj_H[u][v]

            if g_edge != h_edge:
                total_cost += A[min(u, v)][abs(v - u) - 1]
    return total_cost

def solve(adj_G, adj_H, A, N):
    perms = itertools.permutations(range(N))
    
    min_cost = float('inf')
    
    for perm in perms:
        cost = calc(perm, adj_G, adj_H, A, N)
        min_cost = min(min_cost, cost)

    return min_cost

n = int(input())

m_g = int(input())
adj_G = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(m_g):
    u, v = map(int, input().split())
    u -= 1 
    v -= 1
    adj_G[u][v] = adj_G[v][u] = 1


m_h = int(input())
adj_H = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(m_h):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    adj_H[u][v] = adj_H[v][u] = 1
    
cost = [[0 for _ in range(n - 1)] for _ in range(n - 1)]
for i in range(n - 1):
    co = list(map(int, input().split()))
    for j in range(n - i - 1):
        cost[i][j] = co[j]


min_cost = solve(adj_G, adj_H, cost, n)
print(min_cost)
