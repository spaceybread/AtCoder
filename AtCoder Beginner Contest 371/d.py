from bisect import bisect_left, bisect_right



n = int(input())
vil = list(map(int, input().split()))
pop = list(map(int, input().split()))
q = int(input())

quers = []

for i in range(q):
    a, b = map(int, input().split())
    quers.append((a, b))

d = {}

for v in vil:
    d[v] = True

psum = [0] * (n + 1)
for i in range(1, n + 1):
    psum[i] = psum[i - 1] + pop[i - 1]

out = []

for l, r in quers:
    li = bisect_left(vil, l)
    ri = bisect_left(vil, r)
    
    #print(ri, li)
    
    if d.get(r) == True: ri += 1
    
    
    o = 0
    
    if li < ri:
        o = psum[ri] - psum[li]
    
    #o = (r, l, ri, li, o)
    
    out.append(o)

#print(psum)

for l in out:
    print(l)
    pass



    
