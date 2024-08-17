#n = int(input())
n, m = (map(int, input().split()))
a = list(map(int, input().split()))
#b = list(map(int, input().split()))

def solve(cur, N, R, K, idx):
    if idx == N:
        if sum(cur) % K == 0:
            print(*cur)
        return

    for i in range(1, R[idx] + 1):
        cur.append(i)
        solve(cur, N, R, K, idx + 1)
        cur.pop()

solve([], n, a, m, 0)

