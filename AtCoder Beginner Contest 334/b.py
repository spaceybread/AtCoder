import math

ln = input().split()
a = int(ln[0])
m = int(ln[1])
l = int(ln[2]) - a
r = int(ln[3]) - a


trees = r // m - (l - 1) // m
print(trees)
