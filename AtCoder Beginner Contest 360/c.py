import heapq

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

bxs = [[] for _ in range(n)]

for i in range(n):
    heapq.heappush(bxs[a[i] - 1], b[i])

open_slots = set(i for i in range(n) if len(bxs[i]) == 0)
closed = set(i for i in range(n) if len(bxs[i]) == 1)

c = 0

for i in range(n):
    if not open_slots:
        break
    
    if i not in closed:
        while len(bxs[i]) > 1:
            idx = open_slots.pop()
            w = heapq.heappop(bxs[i])
            heapq.heappush(bxs[idx], w)
            c += w
            closed.add(i)
        
print(c)
