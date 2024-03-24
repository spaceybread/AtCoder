#WA

n, k = (map(int, input().split()))

another = []

j = n
while j > 0:
    for i in range(j):
        another.append([str(i + n - j), str(i), str(n - j)])
        if n != j:
            another.append([str(i), str(i + n - j), str(n - j)])
    j -= 1



for i in range(k):
    s = another[i]
    print(" ".join(s))
