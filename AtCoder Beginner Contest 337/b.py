#this code is still terrible, I only needed the last bit not all the contains bs but ok

s = input()
rev = s[::-1]

srt = []
end = []

a = []
if "A" in s:
    a_str = s.index("A")
    a_end = len(s) - rev.index("A")
    srt.append(a_str)
    end.append(a_end)
    i = a_str
    while i < a_end:
        a.append(s[i])
        i = i + 1


b = []
if "B" in s:
    a_str = s.index("B")
    a_end = len(s) - rev.index("B")
    srt.append(a_str)
    end.append(a_end)
    i = a_str
    while i < a_end:
        b.append(s[i])
        i = i + 1

c = []
if "C" in s:
    a_str = s.index("C")
    a_end = len(s) - rev.index("C")
    srt.append(a_str)
    end.append(a_end)
    i = a_str
    while i < a_end:
        c.append(s[i])
        i = i + 1

#print(a, b, c)

if "B" in a or "C" in a or "A" in b or "C" in b or "A" in c or "B" in c:
    print("No")
else:
    for i in range(len(srt) - 1):
        if srt[i + 1] < srt[i]:
            print("No")
            quit()
        if end[i + 1] < end[i]:
            print("No")
            quit()

    print("Yes")
