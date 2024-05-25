#n = int(input())
n, m = (map(int, input().split()))
a = sorted(list(map(int, input().split())))[::-1]
b = sorted(list(map(int, input().split())))[::-1]
#print(a)

prev = None
current = None
for i in range(n + m):
    if len(a) > 0 and len(b) > 0:
        if a[-1] > b[-1]:
            b.pop(-1)
            current = "B"
        else:
            a.pop(-1)
            current = "A"
    else:
        if len(b) == 0 and len(a) > 0:
            a.pop(-1)
            current = "A"
        elif len(a) == 0 and len(b) > 0:
            b.pop(-1)
            current = "B"
    if prev == None:
        prev = current
    else:
        if prev == current and current == "A":
            print("Yes")
            quit()
        else:
            prev = current
            
print("No")
