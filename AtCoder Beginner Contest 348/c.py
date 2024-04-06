#a = list(map(int, input().split()))
n = int(input())
#s = input()

beans = {}

for i in range(n):
    a = list(map(int, input().split()))
    
    if beans.get(a[1]) == None:
        beans[a[1]] = a[0]
    elif beans.get(a[1]) > a[0]:
        beans[a[1]] = a[0]


#print(beans)
v = list(beans.values())

print(max(v))
