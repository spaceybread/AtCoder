n = int(input())
s = input()

i = 0
safe = 0

while i < n - 2:
    if s[i] == 'A':
        safe = i
        if s[i + 1] == 'B':
            if s[i + 2] == 'C':
                print(safe + 1)
                quit()
    i = i + 1

print(-1)
