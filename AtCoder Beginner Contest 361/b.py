#n = int(input())
a, b, c, d, e, f = (map(int, input().split()))
g, h, i, j, k, l = (map(int, input().split()))
#a = list(map(int, input().split()))
#b = list(map(int, input().split()))

cor1 = (a < g < d) and (b < h < e) and (c < i < f)
cor2 = (a < j < d) and (b < k < e) and (c < l < f)

x = a < j and g < d
y = b < k and h < e
z = c < l and i < f

if x and y and z:
    print("Yes")
else:
    print("No")
