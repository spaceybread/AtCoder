import math

n = int(input())

tens = math.floor(n/10) % 10
hunds = math.floor(n/100) % 100

while True:
    #print(hunds*100 + tens*10 + tens*hunds)
    
    if (tens * hunds < 10 and (tens * hunds >= n % 10 or n % 10 == 0)):
        print(hunds*100 + tens*10 + tens*hunds)
        quit()
    else:
        if (tens < 9):
            tens = tens + 1
        else:
            hunds = hunds + 1
            tens = 0
        n = hunds*100 + tens*10 + tens*hunds
        
    
    

