def solve(str):
    i = 1
    while i < len(str):
        if str[i] != "0":
            return False
        i = i + 2
    
    return True
        

if solve(input()):
    print("Yes")
else:
    print("No")





