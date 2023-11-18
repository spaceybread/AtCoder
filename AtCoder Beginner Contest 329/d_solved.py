#from editorial
#https://www.youtube.com/watch?v=boQY9dHyAPI

n, m = map(int, input().split())
a = list(map(int, input().split()))

v = [0] * (n + 1)

top = 0

for x in a:
    v[x] = v[x] + 1
    
    if (v[x] > v[top]) or (v[x] == v[top] and x < top):
        top = x
    print(top)
