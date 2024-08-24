def grund(n):
    if n == 1: return 0
    if n == 2: return 1
    if n % 2 == 1: return 0
    if grund(n // 2) == 0: return 1
    return 0

n = (map(int, input().split()))
a = list(map(int, input().split()))

xs = 0

for num in a:
    xs ^= grund(num)

if xs == 0:
    print("Bruno")
else:
    print("Anna")
