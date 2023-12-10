ln = input().split()
n = int(ln[0])
m = int(ln[1])

s = input()

aval = m
totallog = 0
runlog = 0

for day in s:
    if day == '0':
        aval = m
        runlog = totallog
    
    if day == '1':
        if aval > 0:
            aval = aval - 1
        else:
            
            if runlog > 0:
                runlog = runlog - 1
            
            else:
                totallog = totallog + 1
    
    if day == '2':
        if runlog > 0:
            runlog = runlog - 1
        else:
            totallog = totallog + 1

print(totallog)
