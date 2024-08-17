#n = int(input())
n, k = (map(int, input().split()))
x = list(map(int, input().split()))
a = list(map(int, input().split()))
b = [l for l in a]

for _ in range(k % (2*n)):
    b = [0] * n
    for i in range(n):
        b[i] = a[x[i] - 1]
    a = b
print(*b)
