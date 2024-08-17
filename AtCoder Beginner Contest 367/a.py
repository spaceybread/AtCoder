#n = int(input())
a, b, c = (map(int, input().split()))
#a = list(map(int, input().split()))
#b = list(map(int, input().split()))

f = True

if b > c:
    c += 24

#print(a, b, c)
while b < c:
    if b == a or b == a + 24:
        f = False
        break
    b += 1

if f:
    print("Yes")
else:
    print("No")

