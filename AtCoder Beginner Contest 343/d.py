n, t = map(int, input().split())

sc = [0] * (n)
scores = {0: n}
uniq = 1

for i in range(t):
    a, b = map(int, input().split())

    old = sc[a - 1]
    tba = sc[a - 1] + b
    
    scores[old] = scores.get(old) - 1
    
    if scores.get(old) == 0:
        uniq -= 1
    
    if scores.get(tba) == None:
        uniq += 1
        scores[tba] = 1
    else:
        if scores.get(tba) == 0:
            uniq += 1
        scores[tba] += 1
            
        
    
    sc[a - 1] = tba
    
    print(uniq)
    
    
