#TLE

def c1(s, l, r):
    newString = []

    i = 0

    while i < l - 1:
        newString.append(s[i])
        i = i + 1

    i = l - 1
    while i < r:
        if s[i] == '1':
            newString.append('0')
        else:
            newString.append('1')
        i = i + 1

    while i < len(s):
        newString.append(s[i])
        i = i + 1

    return ("".join(newString))

def c2(s, l, r):
    i = l - 1
    record = 0
    running = 0

    while i < r:
        if s[i] == '1':
            running = running + 1
            if running > record:
                record = running
        else:
            if running > record:
                record = running
            running = 0
        i = i + 1

    return record




lineIn = input().split()
n = int(lineIn[0])
q = int(lineIn[1])

s = input()

q_i = 0

while q_i < q:
    quer = input().split()

    if int(quer[0]) == 1:
        s = c1(s, int(quer[1]), int(quer[2]))

    else:
        print(c2(s, int(quer[1]), int(quer[2])))

    q_i = q_i + 1
