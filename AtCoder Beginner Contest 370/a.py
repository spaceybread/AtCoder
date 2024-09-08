#n = int(input())
n, k = (map(int, input().split()))
#a = list(map(int, input().split()))
#b = list(map(int, input().split()))

if n == 1 and k == 1:
    print("Invalid")
elif n == 1 and k == 0:
    print("Yes")
elif n == 0 and k == 1:
    print("No")
else:
    print("Invalid")
