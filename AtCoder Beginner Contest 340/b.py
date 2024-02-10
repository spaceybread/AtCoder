q = int(input())

reg = []

for _ in range(q):
    com = input().split()
    
    if com[0] == '1':
        reg.append(int(com[1]))
    else:
        print(reg[-int(com[1])])


