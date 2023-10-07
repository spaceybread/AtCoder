def count(str):
    cnt = 0
    i = 0
    while i < len(str):
        if str[i] == "o":
           cnt = cnt + 1
        i = i + 1
    
    return cnt

n = int(input())
i = 0

scores = []

while i < n:
    scores.append(count(input()))
    i = i + 1
    

#print(scores)

out = ""
rank = []
i = 0
while i < n:
    m = max(scores)
    
    rank.append(str(scores.index(m) + 1))
    scores[scores.index(m)] = -1
    
    i = i + 1

print(" ".join(rank))
    
