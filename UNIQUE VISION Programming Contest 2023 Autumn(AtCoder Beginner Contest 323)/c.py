linein = input().split()
n = int(linein[0])
m = int(linein[1])

a = input().split()
i = 0

while i < m:
    a[i] = int(a[i])
    i = i + 1

s = []
scores = []

i = 0
while i < n:
    s.append(input())
    
    scoreIn = 0
    j = 0
    ent = s[i]
    while j < m:
        if ent[j] == "o":
            scoreIn = scoreIn + a[j]
        j = j + 1
    i = i + 1
    scores.append(scoreIn + i)

i = -1
while i < n -1:
    i = i + 1
    if scores[i] == max(scores):
        print(0)
    else:
        count = 0
        b = []
        b_i = 0
        
        while b_i < len(a):
            b.append(a[b_i])
            b_i = b_i + 1
        
        m = max(scores)
        sc = scores[i]
        while sc < m:
            ind = b.index(max(b))
            str = s[i]
            if str[ind] == "x":
                count = count + 1
                sc = sc + max(b)
                b[ind] = -1
            else:
                b[ind] = -1
        print(count)
            
            
        

