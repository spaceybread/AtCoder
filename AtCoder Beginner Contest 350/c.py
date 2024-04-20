n = int(input())
#n, q = (map(int, input().split()))
a = list(map(int, input().split()))
#out = [0] * n
swaps = []
k = 0
#print(out)

while True:
    prev = k
    for i in range(n):
        if i + 1 != a[i]:
            val = a[i]
            valAt = a[val - 1]
        
            a[i] = valAt
            a[val - 1] = val
        
            if (i < val - 1):
                swaps.append([str(i + 1), str(val)])
            else:
                swaps.append([str(val), str(i + 1)])
            k += 1
    if prev == k:
        break
#print(a)
print(k)

for l in swaps:
    print(" ".join(l))
