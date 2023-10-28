lineIn = input().split()
x = int(lineIn[0])
y = int(lineIn[1])

if (x > y):
    if (x - y < 4):
        print("Yes")
    else:
        print("No")
else:
    if (y - x < 3):
        print("Yes")
    else:
        print("No")
