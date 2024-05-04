#n = int(input())
n, x, y, z = (map(int, input().split()))
#a = list(map(int, input().split()))
#b = list(map(int, input().split()))


if x < z < y or y < z < x:
    print("Yes")
else:
    print("No")
