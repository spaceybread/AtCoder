#n = int(input())
#n, m = (map(int, input().split()))
#a = list(map(int, input().split()))
#b = list(map(int, input().split()))

s = input()
up = []
low = []
upcount = 0


for i in range(len(s)):
    if s[i].isupper():
        upcount += 1
    
    up.append(s[i].upper())
    low.append(s[i].lower())
    
if upcount > len(s) - upcount:
    print("".join(up))
else:
    print("".join(low))
