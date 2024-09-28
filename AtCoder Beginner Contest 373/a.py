#n = int(input())
#n, k, m = (map(int, input().split()))
#a = list(map(int, input().split()))
#b = list(map(int, input().split()))
#print(m, k, n)

c = 0
for i in range(1, 13):
    s = input()
    if len(s) == i:
        c += 1
print(c)
