n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

l = int(input())
c = list(map(int, input().split()))

q = int(input())
x = list(map(int, input().split()))

sums = {}

for i in range(n):
    for j in range(m):
        for k in range(l):
            sums[a[i] + b[j] + c[k]] = True

#print(sums)
for x_i in x:
    if sums.get(x_i) != None:
        print("Yes")
    else:
        print("No")
    
