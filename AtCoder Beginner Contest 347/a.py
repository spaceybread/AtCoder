n = list(map(int, input().split()))
a = list(map(int, input().split()))

out = []

for i in range(n[0]):
    if a[i] % n[1] == 0 :
        out.append(str( int(a[i] / n[1])))

print(" ".join(out))
