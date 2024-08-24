n = int(input())
#n, k = (map(int, input().split()))
a = list(map(int, input().split()))
#b = list(map(int, input().split()))

t = 0
for h in a:
    s = (3 - t % 3) % 3
    flag = False
    for i in range(s):
        if i == s - 1:
            h -= 3
            t += 1
        else:
            h -= 1
            t += 1
        if h < 1:
            flag = True
            break
    if flag:
        continue
    
    tri = h // 5
    rem = h % 5
    
    if rem > 3:
        rem = 3
    
    t += tri * 3 + rem

print(t)

