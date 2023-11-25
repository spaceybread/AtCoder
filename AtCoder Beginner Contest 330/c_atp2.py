#WA
import math

def solve(D):
    minV = 2 * 10**12
    
    for i in range(int(math.sqrt(D)) + 1):
        j = int(math.sqrt(D - i**2))
        
        minV = min(minV, abs(i**2 + j**2 - D))
        if j > 0:
                minV = min(minV, abs(i**2 + (-j)**2 - D))
    return minV

print(int(solve(int(input()))))

