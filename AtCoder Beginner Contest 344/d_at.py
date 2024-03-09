#TLE and some random WA

from itertools import product

def build(arr):
    ct = 0
    out = []
    for s in arr:
        if s != "":
            ct += 1
            out.append(s)
    
    outst = "".join(out)
    
    return [ct, outst]

T = input()
N = int(input())

A = [0] * N
S = []

for n in range(N):
    ln = input().split()
    A[n] = int(ln[0])
    
    bag = ["", ]
    for i in range(1, A[n] + 1):
        #print(ln[i])
        bag.append(ln[i])
    S.append(bag)
#print(A)


poss = [list(comb) for comb in list(product(*S))]
#print(poss)
stringset = {}

for l in poss:
    sol = build(l)
    stringset[sol[1]] = sol[0]

#print(stringset)

if stringset.get(T) != None:
    print(stringset[T])
else:
    print(-1)

