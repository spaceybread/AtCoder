from collections import Counter
n = int(input())
#n, k, m = (map(int, input().split()))
#a = list(map(int, input().split()))
#b = list(map(int, input().split()))
#print(m, k, n)

all = []
for _ in range(n * 10):
    all += list(map(int, input().split()))

x = Counter(all)
#print(all)
#print(x)
out = []

for a in all:
    if x[a] > 0.2 * n * 10 and a not in out:
        out.append(a)

if len(out) > 0:
    print(*sorted(out))
else:
    print(-1)
