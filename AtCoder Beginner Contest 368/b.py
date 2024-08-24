n = int(input())
a = list(map(int, input().split()))

t = 0
while sum(1 for x in a if x > 0) > 1:
    a = sorted(a)[::-1]
    a[0] -= 1
    a[1] -= 1
    t += 1
    
print(t)

    
