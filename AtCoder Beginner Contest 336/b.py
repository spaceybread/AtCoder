a = int(input())

if a % 2 == 1:
    print(0)
else:
    n = str(bin(a).replace("0b", ""))
    #print(n)

    i = 1
    
    while n[-i] == '0':
        i = i + 1
    
    print(i - 1)
