#TLE

import math

n = int(input())
a = input().split()
for i in range(n):
    a[i] = int(a[i])

set = [0] * (max(a) + 1)

for i in a:
    for j in range(i):
        set[j] = set[j] + i
    
out = []

for i in range(n):
    out.append(str(set[a[i]]))
        
print(" ".join(out))
