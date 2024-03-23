import itertools

w, b = (map(int, input().split()))

s = "wbwbwwbwbwbw" * 30

for i in range(len(s) - w - b):
    runw = 0
    runb = 0
    for j in range(w + b):
        if s[i + j] == "w":
            runw += 1
        else:
            runb += 1
    #print(runw, runb)
    if runw == w and runb == b:
        print("Yes")
        quit()

print("No")
