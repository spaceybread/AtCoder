#n = int(input())
#n, k, m = (map(int, input().split()))
#a = list(map(int, input().split()))
#b = list(map(int, input().split()))

s = input()
out = []

for i in range(len(s)):
    if s[i] != ".":
        out.append(s[i])

print("".join(out))
