def solve(N, M, S):
    stands = []
    for i in range(N):
        mask = 0
        for j in range(M):
            if S[i][j] == 'o':
                mask |= (1 << j)
        stands.append(mask)
    dp = [float('inf')] * (1 << M)
    dp[0] = 0
    for mask in range(1 << M):
        for stand_mask in stands:
            new_mask = mask | stand_mask
            dp[new_mask] = min(dp[new_mask], dp[mask] + 1)
    return dp[(1 << M) - 1]

#n = int(input())
n, m = (map(int, input().split()))
#a = list(map(int, input().split()))
#b = list(map(int, input().split()))

s = []

for i in range(n):
    s.append(input())
ma = {}



print(solve(n, m, s))
