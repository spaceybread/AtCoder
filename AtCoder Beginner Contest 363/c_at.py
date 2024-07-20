from itertools import permutations
from collections import Counter

def isp(s, k):
    for i in range(len(s) - k + 1):
        sub = s[i:i + k]
        if sub == sub[::-1]:
            return True
    return False

def count(s, k):
    f = Counter(s)
    uc = ''.join(f.keys())
    
    all = set(permutations(s))
    
    val = 0
    for perm in all:
        perm_str = ''.join(perm)
        if not isp(perm_str, k):
            val += 1
    
    return val

n, k = map(int, input().split())
s = input()

print(count(s, k))
