n = int(input())
#n, x, y, z = (map(int, input().split()))
#a = list(map(int, input().split()))
#b = list(map(int, input().split()))

a = []
dict = {}
pos = {}

for i in range(n):
    inp = input().split()
    a.append(int(inp[0]))
    dict[int(inp[0])] = int(inp[1])
    pos[int(inp[0])] = i + 1

ai = sorted(a)[::-1]

keep = [ai[0]]
min = dict[ai[0]]
for i in range(1, n):
    if dict[ai[i]] < min:
        keep.append(ai[i])
        min = dict[ai[i]]

sol = []
for k in keep:
    sol.append(pos[k])

sol = sorted(sol)

print(len(sol))

for p in sol:
    print(p, end= " ")
print()



