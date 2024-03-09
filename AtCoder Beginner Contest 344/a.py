#n, t = map(int, input().split())

s = input()

out = []
ct = 0
for i in range(len(s)):
    if s[i] != "|":
        if ct % 2 == 0:
            out.append(s[i])
    else:
        ct += 1

print("".join(out))
