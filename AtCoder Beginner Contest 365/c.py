#n = int(input())
n, m = (map(int, input().split()))
a = (list(map(int, input().split())))
#b = list(map(int, input().split()))

t = sum(a)

if t <= m:
    print("infinite")
    quit()

l, r = 0, max(a)

while l < r:
    mi = (l + r + 1) // 2
    if sum(min(mi, ai) for ai in a) <= m:
        l = mi
    else:
        r = mi - 1

print(l)
        
