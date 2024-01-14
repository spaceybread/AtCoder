#a couple of questions were based (ha ha) on converting bases so I wrote a base-10 to base-b converter 
#dont know when I might need it

def base(n, b):
    if n == 0:
        return 0
    
    result = ""
    while n > 0:
        r = n % b
        result = str(r) + result
        n //= b
    
    return int(result)

print(base(10, 2))
