#n = int(input())
r, g, b = (map(int, input().split()))
a = input()
#a = list(map(int, input().split()))
#b = list(map(int, input().split()))

if a == 'Red':
    print(min(g, b))
if a == 'Blue':
    print(min(g, r))
if a == 'Green':
    print(min(r, b))
