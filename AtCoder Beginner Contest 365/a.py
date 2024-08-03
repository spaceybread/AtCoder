n = int(input())
#r, g = (map(int, input().split()))
#a = list(map(int, input().split()))
#b = list(map(int, input().split()))

if n % 4 != 0:
    print(365)
else:
    if n % 100 != 0:
        print(366)
    else:
        if n % 400 != 0:
            print(365)
        else:
            print(366)
