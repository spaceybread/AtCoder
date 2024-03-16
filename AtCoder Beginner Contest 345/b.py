#a = list(map(int, input().split()))
import math
n = int(input())

if n < -10:
    last = int(str(n)[-1])
    n = str((n + last))
    out = []
    for i in range(len(n) - 1):
        out.append(n[i])
    print("".join(out))
elif n > 10:
    last = int(str(n)[-1])
    if last != 0:
        n = str((n + 10 - last))
    else:
        n = str(n)
    out = []
    for i in range(len(n) - 1):
        out.append(n[i])
    print("".join(out))
else:
    if n > 0:
        print(1)
    else:
        print(0)
