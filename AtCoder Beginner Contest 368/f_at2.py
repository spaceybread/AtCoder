def grund(n, memo):
    if n in memo:
        return memo[n]
    
    if n % 2 == 1:
        return 0
    
    divisors = []
    x = 1
    while x * x <= n:
        if n % x == 0:
            if x != 1:
                divisors.append(grund(n // x, memo))
            if x != 1 and x != n // x:
                divisors.append(grund(x, memo))
        x += 1
    
    mex_set = [False] * (len(divisors) + 1)
    for g in divisors:
        if g < len(mex_set):
            mex_set[g] = True
    
    mex = 0
    while mex < len(mex_set) and mex_set[mex]:
        mex += 1
    
    memo[n] = mex
    return mex

def compute_game_winner(a):
    memo = {}
    xor_sum = 0
    for num in a:
        xor_sum ^= grund(num, memo)
    return "Bruno" if xor_sum == 0 else "Anna"

n = int(input().strip())
a = list(map(int, input().strip().split()))

print(compute_game_winner(a))
