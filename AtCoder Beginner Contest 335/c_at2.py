class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node([1, 0])

def move(head, direction):
    oldhead = head

    if direction == "R":
        head = Node([oldhead.data[0] + 1, oldhead.data[1]])
    if direction == "L":
        head = Node([oldhead.data[0] - 1, oldhead.data[1]])
    if direction == "U":
        head = Node([oldhead.data[0], oldhead.data[1] + 1])
    if direction == "D":
        head = Node([oldhead.data[0], oldhead.data[1] - 1])
    
    head.next = oldhead
    return head

def find(head, part):
    current = head
    for i in range(part):
        current = current.next
    print(current.data[0], current.data[1])


ln = input().split()
n = int(ln[0])
q = int(ln[1])

current = head

for i in range(n):
    current.next = Node([i + 2, 0])
    current = current.next

current = head

for _ in range(q):
    current = head
    query = input().split()
    
    if query[0] == "1":
        head = move(head, query[1])
    else:
        find(head, int(query[1]) - 1)
        pass
