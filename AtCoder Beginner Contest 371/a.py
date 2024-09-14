#n = int(input())
l = input().split()
#n, k, m = (map(int, input().split()))
#a = list(map(int, input().split()))
#b = list(map(int, input().split()))

m = {}

m["A"] = 0
m["B"] = 0
m["C"] = 0

if l[0] == "<":
    m["B"] += 1
else:
    m["A"] += 1

if l[1] == "<":
    m["C"] += 1
else:
    m["A"] += 1

if l[2] == "<":
    m["C"] += 1
else:
    m["B"] += 1
 
if m["A"] == 1:
    print("A")
elif m["B"] == 1:
    print("B")
else:
    print("C")
