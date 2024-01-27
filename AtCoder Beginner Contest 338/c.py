def solve(Q, A, B, n):
    max_servings = 0
    
    min_A = min(Q[i] // A[i] if A[i] != 0 else float('inf') for i in range(n))
    min_B = min(Q[i] // B[i] if B[i] != 0 else float('inf') for i in range(n))
    
    for k in range(min(min_A, min_B) + 1):
        servings_A = k
        servings_B = min((Q[i] - k * A[i]) // B[i] if B[i] != 0 else float('inf') for i in range(n))
        total_servings = servings_A + servings_B
        max_servings = max(max_servings, total_servings)
    
    return max_servings


n = int(input())
Q = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))


up = solve(Q, A, B, n)
down = solve(Q, B, A, n)

print(max(up, down))
