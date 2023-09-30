lineIn = input().split()
n = int(lineIn[0])
m = int(lineIn[1])
s = input()
t = input()

isSuf = True
isPre = True

i = 0

while i < n:
    if s[i] != t[i]:
        isPre = False
        break
    i = i + 1

base = m - n
i = 0
while i < n:
    if s[i] != t[i + base]:
        isSuf = False
        break
    i = i + 1

if isPre == True and isSuf == True:
    print(0)
elif isPre == True and isSuf == False:
    print(1)
elif isPre == False and isSuf == True:
    print(2)
else:
    print(3)
