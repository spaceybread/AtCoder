n = int(input())
#n, x, y, z = (map(int, input().split()))
#a = list(map(int, input().split()))
#b = list(map(int, input().split()))
s = input()

t = [0] * n
ord = s[::-1]
sol = []
c = 0

for i in range(n):
    if ord[i] == '1':
        r = n - i
        for j in range(r):
            if t[j] == 0:
                c +=1
                t[j] = 1
                sol.append('A')
    else:
        r = n - i
        for j in range(r):
            if t[j] == 1:
                c +=1
                t[j] = 0
                sol.append('B')

print(c)
print("".join(sol))
