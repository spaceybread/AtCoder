#n = int(input())
#a = list(map(int, input().split()))

def check_freq(x):
    freq = {}
    for c in set(x):
       freq[c] = x.count(c)
    return freq

s = input()

alp = check_freq(s)

revalp = {}

for a in alp:
    if revalp.get(alp.get(a)) == None:
        revalp[alp.get(a)] = 1
    else:
        revalp[alp.get(a)] = 1 + revalp.get(alp.get(a))


se = set(revalp.values())

if len(se) == 1 and 2 in se:
    print("Yes")
else:
    print("No")

