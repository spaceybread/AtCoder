n = int(input())
#r, g = (map(int, input().split()))
#a = list(map(int, input().split()))
#b = list(map(int, input().split()))

if n >= 200:
    print(300 - n)
elif 200 > n >= 100:
    print(200 - n)
elif 100 > n >= 1:
    print(100 - n)

