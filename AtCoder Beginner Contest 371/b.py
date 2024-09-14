#n = int(input())
#l = input().split()
n, k = (map(int, input().split()))
#a = list(map(int, input().split()))
#b = list(map(int, input().split()))

m = {}
out = []

for i in range(k):
    it = input().split()
    
    if m.get(it[0]) == None:
        if it[1] == "M":
            out.append("Yes")
            m[it[0]] = True
        else:
            out.append("No")
            m[it[0]] = False
            
    elif m.get(it[0]) == True:
        out.append("No")
    else:
        if it[1] == "M":
            out.append("Yes")
            m[it[0]] = True
        else:
            out.append("No")
            m[it[0]] = False

for l in out:
    print(l)
        
        
    
