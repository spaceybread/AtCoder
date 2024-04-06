#a = list(map(int, input().split()))
n = int(input())
#s = input()

cord = []

for i in range(n):
    cord.append(list(map(int, input().split())))

for i in range(n):
    max = 0
    index = -1
    
    for j in range(n):
        if i != j:
            if (cord[i][0] - cord[j][0])**2 + (cord[i][1] - cord[j][1])**2 > max:
                max = (cord[i][0] - cord[j][0])**2 + (cord[i][1] - cord[j][1])**2
                index = j
    
    print(index + 1)
