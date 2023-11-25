#WA

import math

D = int(input())

d = math.floor(math.sqrt(D))
min = D
i = 0

while i**2 <= D:
    
    c = math.floor(math.sqrt(D - i**2))
    #print(i**2)
    #print(c)
    if c % 1 == 0:
        C = D - i**2 - c**2
        if C < min:
            #print(i**2)
            min = C
            #if min == 0:
             #   print(i)
    
    i = i + 1

print(int(min))

