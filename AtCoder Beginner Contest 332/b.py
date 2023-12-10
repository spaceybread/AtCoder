ln = input().split()
k = int(ln[0])
g = int(ln[1])
m = int(ln[2])


glass = 0
mug = 0

for _ in range(k):
    if glass == g:
        glass = 0
    
    elif mug == 0:
        mug = m
        
    else:
        delta = min(mug, g - glass)
        glass = glass + delta
        mug = mug - delta
    
print(glass, mug)
        
