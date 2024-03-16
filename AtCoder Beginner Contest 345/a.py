#a = list(map(int, input().split()))

s = input()

if s[0] == "<" and s[-1] == ">":
    for i in range(1, len(s) - 1):
        if s[i] != "=":
            print("No")
            quit()
else:
    print("No")
    quit()
    
print("Yes")

