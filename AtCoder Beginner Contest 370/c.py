#n = int(input())
#n, k = (map(int, input().split()))
#a = list(map(int, input().split()))
#b = list(map(int, input().split()))
s = list(input())
t = list(input())

x = []

for i in range(len(s)):
    if s[i] != t[i] and t[i] < s[i]:
        s[i] = t[i]
        x.append("".join(s))

for i in range(len(s) - 1, -1, -1):
    if s[i] != t[i]:
        s[i] = t[i]
        x.append("".join(s))

print(len(x))
for w in x: print(w)
