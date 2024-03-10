#I mean can you even really call this an attempt?     

import math

def order(n):
    return math.floor(math.log(n, 10))

finalList = [0, 0, 9, 180, 2619, 33570, 402129, 4619160, 51572439, 564151950, 6077367549, 64696307940, 682266771459, 7140400943130, 74263608488169]

def compute(k, l):
    runn = k
    O = order(k)
    
    while O > 0:
        
        a = int(k / 10**(O- 1))
        runn = runn + a*l[O]
        O -= 1
    print(k, runn)
        
    return O

print(compute(int(input()), finalList))
