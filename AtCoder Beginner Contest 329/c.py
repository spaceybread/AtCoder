#WA

n = int(input())
S = input()

s = [0] * n

for i in range(n):
    if i >= n - 1:
        s[i] = s[i- 1] + (1)
    else:
        s[i + 1] = s[i] + (S[i] == S[i + 1])
    

lset = set(s)
s = list(lset)
print(len(s))
