#n = int(input())
n, k = (map(int, input().split()))
a = list(map(int, input().split()))
#b = list(map(int, input().split()))
ma = sorted(a)
m = n - k - 1
delta = 2**32 - 1

for i in range(n):
    if m + i >= n:
        continue
    
    d = ma[m + i] - ma[i]
    
    if delta > d:
        delta = d

print(delta)
