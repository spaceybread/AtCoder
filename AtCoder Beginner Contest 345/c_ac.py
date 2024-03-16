# I hate myself

s = input()
dict = {}

tot = 0
flag = False
for i in range(len(s)):
    if dict.get(s[i]) == None:
        dict[s[i]] = 1
    else:
        dict[s[i]] += 1
        flag = True


for i in dict:
    tot += int(dict.get(i) * (len(s) - dict.get(i)))
 
if flag == True:
    print(int(tot/2) + 1)
else:
    print(int(tot/2))





