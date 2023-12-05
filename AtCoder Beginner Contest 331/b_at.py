#WA

import math

ln = input().split()
N = int(ln[0])
S = int(ln[1]) #6 eggs
M = int(ln[2]) #8 eggs
L = int(ln[3]) #12 eggs

lol = [math.ceil(N/6) * S, math.ceil(N/8) * M, math.ceil(N/12) * L]


for s in range(math.ceil(N/6)):
    for e in range(math.ceil(N/8)):
        for t in range(math.ceil(N/12)):
            current_sum = 6*s + 8*e + 12*t
            if current_sum >= N:

                lol.append(S*s + M*e + L*t)
            else:
                break

    

#print(lol)
print(min(lol))
