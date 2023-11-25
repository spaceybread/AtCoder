ln = input().split()
n = int(ln[0])
l = int(ln[1])
r = int(ln[2])

aN = input().split()
results = []

for i in range(n):
    a = int(aN[i])
    
    if a <= l:
        results.append(str(l))
    elif a >= r:
        results.append(str(r))
    else:
        results.append(str(a))
        
print(" ".join(results))
        
