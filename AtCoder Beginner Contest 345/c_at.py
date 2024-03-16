#WA

#a = list(map(int, input().split()))
s = input()

dict = {}

for i in range(len(s)):
    if dict.get(s[i]) == None:
        dict[s[i]] = 1
    else:
        dict[s[i]] += 1

#print(dict)

tot = 0
for i in dict:
    tot += dict.get(i) * (len(s) - dict.get(i))
    
if tot == 0:
    print(1)
    quit()
print(int(tot/2))


