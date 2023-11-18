# TLE

lineIn = input().split()
n = int(lineIn[0])
m = int(lineIn[1])

players = []

for i in range(n):
    players.append(0)


a = input().split()

for i in range(m):
    ind = int(a[i]) - 1
    players[ind] = players[ind] + 1
    print(players.index(max(players)) + 1)
