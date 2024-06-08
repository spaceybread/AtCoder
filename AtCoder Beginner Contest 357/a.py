#n = int(input())
n, m = (map(int, input().split()))
a = list(map(int, input().split()))
#b = list(map(int, input().split()))

if sum(a) < m:
    print(n)
    quit()

for i in range(n):
    m -= a[i]
    
    if m == 0:
        print(i + 1)
        quit()
        
    if m < 0:
        print(i)
        quit()
    
