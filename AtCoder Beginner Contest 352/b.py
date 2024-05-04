#n = int(input())
#n, x, y, z = (map(int, input().split()))
#a = list(map(int, input().split()))
#b = list(map(int, input().split()))


s = input()
t = input()

idx = 0
sol = []
for i in range(len(s)):
    while s[i] != t[idx]:
        idx += 1
    sol.append(str(idx + 1))
    idx += 1
    
print(" ".join(sol))
