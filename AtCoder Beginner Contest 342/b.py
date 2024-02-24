n = int(input())
p = list(map(int, input().split()))
q = int(input())

for quer in range(q):
    ln = list(map(int, input().split()))
    
    for i in p:
        if i == ln[0] or i == ln[1]:
            print(i)
            break
    
