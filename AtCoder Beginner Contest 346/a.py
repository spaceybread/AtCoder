n = int(input())
a = list(map(int, input().split()))

out = []

for i in range(n - 1):
    out.append(str(a[i] * a[i + 1]))
    
print(" ".join(out))
