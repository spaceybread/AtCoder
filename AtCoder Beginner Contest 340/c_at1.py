#fails sample case 3

import math

def rec(n, arr):
    a = 0
    b = 0
    if math.floor(n/2) > 1:
        if (arr[math.floor(n/2)] != 0):
            a = arr[math.floor(n/2)]
        else:
            a = rec(math.floor(n/2), arr)
            arr[math.floor(n/2)] = a
    if math.ceil(n/2) > 1:
        if (arr[math.ceil(n/2)] != 0):
            b = arr[math.ceil(n/2)]
        else:
            b = rec(math.ceil(n/2), arr)
            arr[math.ceil(n/2)] = b
        
    return n + a + b

n = int(input())

arr = [0] * n

print(rec(n, arr))
