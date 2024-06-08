def inv(a, p):
    return pow(a, p - 2, p)

def solve(n, p):
    sN = str(n)
    
    pd = pow(10, len(sN), p)
    pdn = pow(pd, n, p)
    
    denom = (pd - 1) % p
    denom = inv(denom, p)
    
    return (n * ((pdn - 1) % p) * denom) % p

n = int(input())

print(solve(n, 998244353))

#n, m = (map(int, input().split()))
#a = list(map(int, input().split()))
#b = list(map(int, input().split()))

