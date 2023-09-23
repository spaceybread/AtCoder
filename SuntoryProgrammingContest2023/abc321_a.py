n = input()
leg = len(n)

if len == 1:
    print("Yes")
    quit()
else:
    i = 0

    while i+1 < leg:
        if int(n[i]) > int(n[i + 1]):
            i = i + 1
        else:
            print("No")
            quit()

    print("Yes")
