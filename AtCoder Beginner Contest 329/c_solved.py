#from editorial 
#https://www.youtube.com/watch?v=boQY9dHyAPI

import collections
import itertools

n = int(input())
s = input()

d = collections.defaultdict(int)

for c, g in itertools.groupby(s):
    d[c] = max(d[c], len(list(g)))

print(sum(d.values()))
