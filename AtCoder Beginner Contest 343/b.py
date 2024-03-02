n = int(input())

mat = []
for i in range(n):
    mat.append(list(map(int, input().split())))

for i in mat:
    line = []
    for j in range(n):
        if i[j] == 1:
            line.append(str(j + 1))
    print(" ".join(line))
