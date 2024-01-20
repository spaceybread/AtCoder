#terrible code: WA

s = input()

if s == "":
    print("Yes")
    quit()


if "A" in s and "B" in s and "C" in s:
    if s.index("A") > s.index("B") or s.index("A") > s.index("C") or s.index("B") > s.index("C"):
        print("No")
    else:
        s = s [::-1]
        if s.index("C") > s.index("A") or s.index("C") > s.index("B") or s.index("B") > s.index("A"):
            print("No")
        else:
            print("Yes")
else:
    if "A" in s:
        if "B" in s:
            if s.index("A") > s.index("B"):
                print("No")
            else:
                s = s[::-1]
                if s.index("B") > s.index("A"):
                    print("No")
                else:
                    print("Yes")
        elif "C" in s:
            if s.index("A") > s.index("C"):
                print("No")
            else:
                s = s[::-1]
                if s.index("C") > s.index("A"):
                    print("No")
                else:
                    print("Yes")
        else:
            print("Yes")
    else:
        if "B" in s:
            if "C" in s:
                if s.index("B") > s.index("C"):
                    print("No")
                else:
                    s = s[::-1]
                    if s.index("C") > s.index("B"):
                        print("No")
                    else:
                        print("Yes")
            else:
                print("Yes")
        else:
            print("Yes")
    
