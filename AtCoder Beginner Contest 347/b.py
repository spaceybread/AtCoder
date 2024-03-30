s = input()

l = []

for i in range(1, len(s) + 1):
    for j in range(len(s) - i + 1):
        
        n = j + i - 1
        out = []
        for k in range(j, n + 1):
            out.append(s[k])
        #print(out)
        l.append("".join(out))
        
a = set(l)
print(len(a))
