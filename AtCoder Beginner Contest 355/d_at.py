n = int(input())


a = []
b = []


for i in range(n):
    a.append((list(map(int, input().split()))))

a = sorted(a)
c = 0

for left in range(n - 1):
    check = a[left]
    
    for j in range(left + 1, n):
        if check[1] >= a[j][0]:
            #print(check, a[j])
            c += 1
        else:
            break
print(c)
    

