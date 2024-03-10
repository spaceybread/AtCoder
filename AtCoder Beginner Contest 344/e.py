class Node:
    def __init__(self, val, back = None, front = None):
        self.val = val
        self.front = front
        self.back = back

n = int(input())
a = list(map(int, input().split()))
q = int(input())

map1 = {}

prev = None
root = None
for i in a:
    link = Node(i, prev, None)
        
    if link.back == None:
        root = link
        
    map1[i] = link
    if prev != None:
        prev.front = link
    prev = link

for i in range(q):
    quer = list(map(int, input().split()))
    
    if quer[0] == 1:
        back = map1.get(quer[1])
        front = back.front
        
        link = Node(quer[2], back, front)
        back.front = link
        if front != None:
            front.back = link
        map1[quer[2]] = link
        
    else:
        link = map1.get(quer[1])
        back = link.back
        front = link.front
        
        if back == None:
            root = front
            root.back = None
        elif front == None:
            back.front = None
        else:
            front.back = back
            back.front = front
            
        
        map1[quer[1]] = None
        

cur = root
out = []

while cur != None:
    out.append(str(cur.val))
    cur = cur.front

print(" ".join(out[::1]))
