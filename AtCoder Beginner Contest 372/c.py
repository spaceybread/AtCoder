import math
#n = int(input())
#a = list(map(int, input().split()))
#b = list(map(int, input().split()))

n, q = (map(int, input().split()))
s = list(input())
quer = []
for i in range(q):
    x, c = input().split()
    quer.append((int(x) - 1, c))




count = 0
for i in range(n - 2):
    if s[i:i+3] == ["A", "B", "C"]: count += 1

for xi, ci in quer:
    start, end = max(0, xi - 2), min(n - 1, xi + 2)
    
    for i in range(start, end):
        if s[i:i+3] == ["A", "B", "C"]:
            count += -1
    
    s[xi] = ci
    
    for i in range(start, end):
        if s[i:i+3] == ["A", "B", "C"]:
            count += 1
        
    print(count)
