s = input()
t = input().lower()

flag = True

if t[2] == 'x':
    if t[0] in s:
        i = s.index(t[0]) + 1
        s = s[i::]
        if t[1] in s:
            print("Yes")
            quit()
    
    print("No")
else:
    if t[0] in s:
        i = s.index(t[0]) + 1
        s = s[i::]
        if t[1] in s:
            i = s.index(t[1]) + 1
            s = s[i::]
            if t[2] in s:
                print("Yes")
                quit()
    print("No")
