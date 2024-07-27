n, x, y = map(int, input().split())
a, b = [], []

for _ in range(n):
    l, m = map(int, input().split())
    a.append(l)
    b.append(m)

def max_dishes(N, A, B, X, Y):
    dp = [[[-1 for _ in range(Y + 1)] for _ in range(X + 1)] for _ in range(N + 1)]
    dp[0][0][0] = 0

    for i in range(1, N + 1):
        for s in range(X + 1):
            for l in range(Y + 1):
                if dp[i-1][s][l] != -1:
                    dp[i][s][l] = max(dp[i][s][l], dp[i-1][s][l])
                    
                    if s + A[i-1] <= X and l + B[i-1] <= Y:
                        dp[i][s + A[i-1]][l + B[i-1]] = max(dp[i][s + A[i-1]][l + B[i-1]], dp[i-1][s][l] + 1)

    max_dishes_eaten = 0
    for s in range(X + 1):
        for l in range(Y + 1):
            if dp[N][s][l] != -1:
                max_dishes_eaten = max(max_dishes_eaten, dp[N][s][l])

    return max_dishes_eaten

o = max_dishes(n, a, b, x, y)
if o == n:
    print(o)
else:
    print(o + 1)
