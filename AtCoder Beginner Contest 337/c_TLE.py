#I half knew this was wrong as I wrote it because I was using index() but I thought it was worth to shot to check for WAs

n = int(input())
a = input().split()

for _ in range(n):
    a[_] = int(a[_])

ord = [a.index(-1) + 1]

for i in range(n - 1):
    ln = a.index(ord[i]) + 1
    ord.append(ln)


print(*ord, sep = " ") 
