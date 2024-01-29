#came back to it after a bit of time, I think I was stupid when I first attempted this

n = int(input())
ins = list(map(int, input().split()))
vals = sorted(ins)
vals = vals[::-1]
#print(vals)

sum = 0
sumfn = 0
dict = {}


for i in range(vals[0] + 1):
    dict[i] = -1

for i in range(n):
    if dict.get(vals[i]) == -1:
        dict[vals[i]] = sum
        
    sum = sum + vals[i]
    
ans = []

for i in ins:
    ans.append(str(dict.get(i)))
    
print(" ".join(ans))
