def base5(n):
    if n == 0:
        return 0
    
    result = ""
    while n > 0:
        r = n % 5
        result = str(r) + result
        n //= 5
    
    return int(result)

ln = int(input()) - 1
print(((base5(ln)) * 2))
