#n = int(input())
#a = list(map(int, input().split()))
s = input()

st = []
num = []
for i in range(3):
    st.append(s[i])
for i in range(3, 6):
    num.append(s[i])

abc = "".join(st)
n = int("".join(num))

if abc == "ABC":
    if n < 350 and n > 0 and n != 316:
        print("Yes")
        quit()
print("No")
