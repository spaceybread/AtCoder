mat = []

for _ in range(9):
    lineIn = input().split()
    a = []
    for i in range(9):
        a.append(int(lineIn[i]))

    mat.append(a)


for a in mat:
    if (sum(a) != 45):
        print("No")
        quit()

    for i in range(9):
        if a.count(i + 1) != 1:
            print("No")
            quit()

#[down][right]

sum = mat[0][0] + mat[0][1] + mat[0][2] + mat[1][0] + mat[2][0] + mat[1][1] + mat[1][2] + mat[2][1] + mat[2][2]
box = [mat[0][0] , mat[0][1] , mat[0][2] , mat[1][0] , mat[2][0] , mat[1][1] , mat[1][2] , mat[2][1] , mat[2][2]]
if (sum != 45):
    print("No")
    quit()
for i in range(9):
    if box.count(i + 1) != 1:
        print("No")
        quit()

sum = mat[3][0] + mat[3][1] + mat[3][2] + mat[4][0] + mat[5][0] + mat[4][1] + mat[4][2] + mat[5][1] + mat[5][2]
box = [mat[3][0] , mat[3][1] , mat[3][2] , mat[4][0] , mat[5][0] , mat[4][1] , mat[4][2] , mat[5][1] , mat[5][2]]
if (sum != 45):
    print("No")
    quit()
for i in range(9):
    if box.count(i + 1) != 1:
        print("No")
        quit()

sum = mat[6][0] + mat[6][1] + mat[6][2] + mat[7][0] + mat[8][0] + mat[7][1] + mat[7][2] + mat[8][1] + mat[8][2]
box = [mat[6][0] , mat[6][1] , mat[6][2] , mat[7][0] , mat[8][0] , mat[7][1] , mat[7][2] , mat[8][1] , mat[8][2]]
if (sum != 45):
    print("No")
    quit()
for i in range(9):
    if box.count(i + 1) != 1:
        print("No")
        quit()
#

sum = mat[0][3] + mat[0][4] + mat[0][5] + mat[1][3] + mat[2][3] + mat[1][4] + mat[1][5] + mat[2][4] + mat[2][5]
box = [mat[0][3] , mat[0][4] , mat[0][5] , mat[1][3] , mat[2][3] , mat[1][4] , mat[1][5] , mat[2][4] , mat[2][5]]
if (sum != 45):
    print("No")
    quit()
for i in range(9):
    if box.count(i + 1) != 1:
        print("No")
        quit()

sum = mat[3][3] + mat[3][4] + mat[3][5] + mat[4][3] + mat[5][3] + mat[4][4] + mat[4][5] + mat[5][4] + mat[5][5]
box = [mat[3][3] , mat[3][4] , mat[3][5] , mat[4][3] , mat[5][3] , mat[4][4] , mat[4][5] , mat[5][4] , mat[5][5]]

if (sum != 45):
    print("No")
    quit()
for i in range(9):
    if box.count(i + 1) != 1:
        print("No")
        quit()

sum = mat[6][3] + mat[6][4] + mat[6][5] + mat[7][3] + mat[8][3] + mat[7][4] + mat[7][5] + mat[8][4] + mat[8][5]
box = [mat[6][3] , mat[6][4] , mat[6][5] , mat[7][3] , mat[8][3] , mat[7][4] , mat[7][5] , mat[8][4] , mat[8][5]]
if (sum != 45):
    print("No")
    quit()
for i in range(9):
    if box.count(i + 1) != 1:
        print("No")
        quit()

sum = mat[0][6] + mat[0][7] + mat[0][8] + mat[1][6] + mat[2][6] + mat[1][7] + mat[1][8] + mat[2][7] + mat[2][8]
box = [mat[0][6] , mat[0][7] , mat[0][8] , mat[1][6] , mat[2][6] , mat[1][7] , mat[1][8] , mat[2][7] , mat[2][8]]
if (sum != 45):
    print("No")
    quit()
for i in range(9):
    if box.count(i + 1) != 1:
        print("No")
        quit()

sum = mat[3][6] + mat[3][7] + mat[3][8] + mat[4][6] + mat[5][6] + mat[4][7] + mat[4][8] + mat[5][7] + mat[5][8]
box = [mat[3][6] , mat[3][7] , mat[3][8] , mat[4][6] , mat[5][6] , mat[4][7] , mat[4][8] , mat[5][7] , mat[5][8]]
if (sum != 45):
    print("No")
    quit()

sum = mat[6][6] + mat[6][7] + mat[6][8] + mat[7][6] + mat[8][6] + mat[7][7] + mat[7][8] + mat[8][7] + mat[8][8]
box = [mat[6][6] , mat[6][7] , mat[6][8] , mat[7][6] , mat[8][6] , mat[7][7] , mat[7][8] , mat[8][7] , mat[8][8]]
if (sum != 45):
    print("No")
    quit()
for i in range(9):
    if box.count(i + 1) != 1:
        print("No")
        quit()


for i in range(9):
    sum = 0
    a = []
    for j in range(9):
        sum = mat[j][i] + sum
        a.append(mat[j][i])

    if (sum != 45):
        print("No")
        quit()

    for i in range(9):
        if a.count(i + 1) != 1:
            print("No")
            quit()

fullNum = []

for i in range(9):
    for j in range(9):
        fullNum.append(mat[j][i])

for i in range(9):
    if (fullNum.count(i + 1) != 9):
        print("No")
        quit()


print("Yes")


#print(mat)
