n = int(input())
s = input()
q = int(input())

pos = {char: char for char in "abcdefghijklmnopqrstuvwxyz"}

for _ in range(q):
    ln = input().split()
    c = ln[0]
    d = ln[1]
    
    for k, v in pos.items():
            if v == c:
                pos[k] = d
    
out = []
for i in range(n):
    out.append(pos[s[i]])

print("".join(out))


#damn 
