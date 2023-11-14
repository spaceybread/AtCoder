lineIn = input().split()
n = int(lineIn[0])
x = int(lineIn[1])

scoresS = input().split()

sum = 0
for i in range(n):
    if int(scoresS[i]) <= x:
        sum = int(scoresS[i]) + sum

print(sum)
