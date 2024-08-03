n = int(input())
s = input()

prev, c = "", 0

for i in range(n):
    tak = s[i]
    
    if tak == "R":
        if prev == "P":
            prev = "R"
        else:
            prev = "P"
            c += 1
    
    if tak == "P":
        if prev == "S":
            prev = "P"
        else:
            prev = "S"
            c += 1
    
    if tak == "S":
        if prev == "R":
            prev = "S"
        else:
            prev = "R"
            c += 1

print(c)

