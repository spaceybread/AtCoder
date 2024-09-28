#n = int(input())
#n, k, m = (map(int, input().split()))
#a = list(map(int, input().split()))
#b = list(map(int, input().split()))
#print(m, k, n)

ord = list("BCDEFGHIJKLMNOPQRSTUVWXYZ")

s = list(input())
ke = {}

for i in range(26):
    ke[s[i]] = i

c = 0
prev = ke["A"]

for a in ord:
    c += abs(ke[a] - prev)
    prev = ke[a]

print(c)
