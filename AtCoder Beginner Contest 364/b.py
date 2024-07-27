#n = int(input())
h, w = (map(int, input().split()))
si, sj = (map(int, input().split()))
si -= 1
sj -= 1

mp = []

for _ in range(h):
    mp.append(list(input()))

x = list(input())

for d in x:
    if d == "U":
        if si == 0 or mp[si - 1][sj] == '#':
            pass
        else:
            si -= 1
    
    if d == "D":
        if si == h - 1 or mp[si + 1][sj] == '#':
            pass
        else:
            si += 1
            
    if d == "L":
        if sj == 0 or mp[si][sj - 1] == '#':
            pass
        else:
            sj -= 1
    
    if d == "R":
        if sj == w - 1 or mp[si][sj + 1] == '#':
            pass
        else:
            sj += 1

print(si + 1, sj + 1)

#a = list(map(int, input().split()))
#b = list(map(int, input().split()))

