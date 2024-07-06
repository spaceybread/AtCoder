def counter(s):
    w, b = s.count('W'), s.count('B')
    return w, b

def poss(s, t):
    w_s, b_s = counter(s)
    w_t, b_t = counter(t)
    
    return w_s == w_t and b_s == b_t
    
n = int(input())
#n, k = (map(int, input().split()))
#a = list(map(int, input().split()))
#b = list(map(int, input().split()))
s = list(input())
t = list(input())

if poss(s, t):
    c, i, j = 0, 0, 0
    
    while i < n and j < n:
        if s[i] == t[j]:
            i += 1
            j += 1
            
        else:
            if s[i] == 'W' and t[j] == 'B':
                while i < n and s[i] != 'B':
                    i += 1
                while j < n and t[j] != 'W':
                    j += 1
            elif s[i] == 'B' and t[j] == 'W':
                while i < n and s[i] != 'W':
                    i += 1
                while j < n and t[j] != 'B':
                    j += 1
            
            if i < n and j < n and s[i] != t[j]:
                s[i], s[j] = s[j], s[i]
                c += 1
                i += 1
                j += 1
    
    #print(s)
    #print(t)
    print(c + 3)
else:
    print(-1)
