#n = int(input())
n, k = (map(int, input().split()))
a = list(map(int, input().split()))
#b = list(map(int, input().split()))

k = n - k
b = a[k:n] + a[0:k]
print(*b)

