def solve(S, T):
    n = len(S)
    len_T = len(T)
    
    for w in range(1, n):
        for c in range(1, w + 1):
            result = []
            for i in range(0, n, w):
                substring = S[i:i+w]
                if len(substring) >= c:
                    result.append(substring[c-1])
            if ''.join(result) == T:
                return "Yes"
    
    return "No"

s, t = (input().split())
print(solve(s, t))

