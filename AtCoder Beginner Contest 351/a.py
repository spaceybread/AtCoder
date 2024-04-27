#n = int(input())
#n, q = (map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))

A = 0
B = 0

for i in a:
    A += i
for j in b:
    B += j

print(A - B + 1)
