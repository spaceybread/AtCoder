n = int(input())
a = list(map(int, input().split()))

for i in range(n - 1):
    q = list(map(int, input().split()))
    wal = a[i]
    
    run = 0
    
    k = wal // q[0]
    run = k * q[1]
        
    a[i + 1] = a[i + 1] + run

print(a[-1])

