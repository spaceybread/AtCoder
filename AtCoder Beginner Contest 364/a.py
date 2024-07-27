n = int(input())
#r, g = (map(int, input().split()))
#a = list(map(int, input().split()))
#b = list(map(int, input().split()))

prev = None
sick = False

out = "Yes"
for _ in range(n):
    if sick:
        out = "No"
    s = input()
    if s == prev and s == "sweet":
        sick = True
    prev = s

print(out)


