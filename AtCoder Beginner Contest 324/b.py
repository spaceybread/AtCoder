n = int(input())

while n % 2 == 0:
    n = n / 2

while n % 3 == 0:
    n = n / 3

if n == 1:
    print("Yes")
else:
    print("No")
