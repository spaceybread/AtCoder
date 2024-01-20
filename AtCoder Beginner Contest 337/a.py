n = int(input())

t = 0
a = 0

for _ in range(n):
    ln = input().split()
    t = t + int(ln[0])
    a = a + int(ln[1])

if t > a:
    print("Takahashi")
elif a > t:
    print("Aoki")
else:
    print("Draw")
