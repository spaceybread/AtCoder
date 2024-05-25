#n = int(input())
#n, x, y, z = (map(int, input().split()))
a = list(map(int, input().split()))
#b = list(map(int, input().split()))
#print(a)
sus = [False] * 3

c = 0
if 1 in a:
    sus[0] = True
    c += 1
if 2 in a:
    sus[1] = True
    c += 1
if 3 in a:
    sus[2] = True
    c += 1

if c == 2:
    for i in range(3):
        if sus[i] == False:
            print(i + 1)
            quit()
else:
    print(-1)


