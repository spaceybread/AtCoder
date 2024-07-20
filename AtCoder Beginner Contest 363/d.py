def solve(n):
    if n <= 2:
        return n - 1
    
    s = str(n)
    d = len(s) - 1
    
    if '11' <= s <= '2':
        rev = -1
    else:
        rev = -2
    
        if s < '2':
            d -= 1
    
    p = str(n - 10**d)
    p += p[rev::-1]
    
    return int(p)

print(solve(int(input())))
