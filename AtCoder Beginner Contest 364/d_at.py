import bisect
import heapq

n, q = map(int, input().split())
al = sorted(map(int, input().split()))

#n, q = 10**5, 10**4
#al = [2*a for a in range(10**5)]
#bl = [a+1 for a in range(10**4)]
#kl = [a + 5 for a in range(10**4)]

out = []

for _ in range(q):
    b, k = map(int, input().split())
    
    #b, k = bl[_], kl[_]
    
    p = bisect.bisect_left(al, b)
    l, r = p - 1, p
    
    max_heap = []
    
    while len(max_heap) < k and (l >= 0 or r < n):
        if l >= 0 and (r >= n or abs(al[l] - b) <= abs(al[r] - b)):
            heapq.heappush(max_heap, -abs(al[l] - b))
            l -= 1
        elif r < n:
            heapq.heappush(max_heap, -abs(al[r] - b))
            r += 1
            
        if len(max_heap) > k:
            heapq.heappop(max_heap)
    
    out.append(-heapq.heappop(max_heap))
    
for result in out:
    print(result)
