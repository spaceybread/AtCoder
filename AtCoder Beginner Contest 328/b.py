#this is the worst piece of code I've ever written

n = int(input())

ds = input().split()

count = 0

A1set = [1, 11]
A2set = [2, 22]
A3set = [3, 33]
A4set = [4, 44]
A5set = [5, 55]
A6set = [6, 66]
A7set = [7, 77]
A8set = [8, 88]
A9set = [9, 99]

fullStack = [A1set, A2set, A3set, A4set, A5set, A6set, A7set, A8set, A9set]

for i in range(n):
    if i < 9:
        #print(i)
        testSet = [fullStack[i][0], fullStack[i][1]]
        
        if int(ds[i]) >= testSet[0]:
            count = count + 1
            #print(testSet)
        
        if int(ds[i]) >= testSet[1]:
            count = count + 1
            #print(testSet)
            
    elif (i == 10):
        testSet = [fullStack[i % 10][0], fullStack[i % 10][1]]
        
        if int(ds[i]) >= testSet[0]:
            count = count + 1
            #print(testSet)
        
        if int(ds[i]) >= testSet[1]:
            count = count + 1
            #print(testSet)
    
    elif (i == 21):
        testSet = [fullStack[i % 10][0], fullStack[i % 10][1]]
        
        if int(ds[i]) >= testSet[0]:
            count = count + 1
            #print(testSet)
        
        if int(ds[i]) >= testSet[1]:
            count = count + 1
            #print(testSet)
    
    elif (i == 32):
        testSet = [fullStack[i % 10][0], fullStack[i % 10][1]]
        
        if int(ds[i]) >= testSet[0]:
            count = count + 1
            #print(testSet)
        
        if int(ds[i]) >= testSet[1]:
            count = count + 1
            #print(testSet)
    
    elif (i == 43):
        testSet = [fullStack[i % 10][0], fullStack[i % 10][1]]
        
        if int(ds[i]) >= testSet[0]:
            count = count + 1
            #print(testSet)
        
        if int(ds[i]) >= testSet[1]:
            count = count + 1
            #print(testSet)
        
    elif (i == 54):
        
        testSet = [fullStack[i % 10][0], fullStack[i % 10][1]]
        
        if int(ds[i]) >= testSet[0]:
            count = count + 1
            #print(testSet)
        
        if int(ds[i]) >= testSet[1]:
            count = count + 1
            #print(testSet)
        
    elif (i == 65):
        testSet = [fullStack[i % 10][0], fullStack[i % 10][1]]
        
        if int(ds[i]) >= testSet[0]:
            count = count + 1
            #print(testSet)
        
        if int(ds[i]) >= testSet[1]:
            count = count + 1
            #print(testSet)
        
    
    elif (i == 76):
        
        testSet = [fullStack[i % 10][0], fullStack[i % 10][1]]
        
        if int(ds[i]) >= testSet[0]:
            count = count + 1
            #print(testSet)
        
        if int(ds[i]) >= testSet[1]:
            count = count + 1
            #print(testSet)

    
    elif (i == 87):
        testSet = [fullStack[i % 10][0], fullStack[i % 10][1]]
        
        if int(ds[i]) >= testSet[0]:
            count = count + 1
            #print(testSet)
        
        if int(ds[i]) >= testSet[1]:
            count = count + 1
            #print(testSet)
        
        
    elif (i == 98):
        testSet = [fullStack[i % 10][0], fullStack[i % 10][1]]
        
        if int(ds[i]) >= testSet[0]:
            count = count + 1
            #print(testSet)
        
        if int(ds[i]) >= testSet[1]:
            count = count + 1
            #print(testSet)
    
        
    
print(count)

