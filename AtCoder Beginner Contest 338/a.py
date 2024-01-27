s = input()

if s[0].islower():
    print("No")
    quit()

for i in range(len(s) - 1):
    if s[i + 1].isupper():
        print("No")
        quit()

print("Yes")

