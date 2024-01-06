#TLE

def move(drag, direction):
    
    for i in range(len(drag) - 1):
        drag[len(drag) - 1 - i][0] = drag[len(drag) - i - 2][0]
        drag[len(drag) - 1 - i][1] = drag[len(drag) - i - 2][1]
    
    if direction == "R":
        drag[0][0] = drag[0][0] + 1
    if direction == "L":
        drag[0][0] = drag[0][0] - 1
    if direction == "U":
        drag[0][1] = drag[0][1] + 1
    if direction == "D":
        drag[0][1] = drag[0][1] - 1

ln = input().split()
n = int(ln[0])
q = int(ln[1])

dragon = []

for i in range(n):
    dragon.append([i + 1, 0])

for _ in range(q):
    #print(dragon)
    #print()
    qu = input().split()
    
    if qu[0] == "1":
        move(dragon, qu[1])
    else:
        print(dragon[int(qu[1]) - 1][0], dragon[int(qu[1]) - 1][1])
        #pass
    
    
