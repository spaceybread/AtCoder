x1, y1, x2, y2 = (map(int, input().split()))
#a = list(map(int, input().split()))
#b = list(map(int, input().split()))

w = abs(x2 - x1)
h = abs(y2 - y1)

wr = w % 4
hr = h % 2

addedh = 0
addedw = 0

if hr == 1:
    addedh = w / 2

if wr == 1:
    addedw = (3/4) * h * 1
elif wr == 2:
    addedw = (3/4) * h * 2
elif wr == 3:
    addedw = (3/4) * h * 2
    addedw += (1/4) * h * 1

inter = 0

if hr != 0 and wr != 0:
    if wr == 1:
        inter = -0.5
    elif wr == 2:
        inter = -0.75
    elif wr == 3:
        inter = -0.75


w -= wr
h -= hr
a = (w * h * 0.5) + addedh + addedw + inter * 4

a = a * 2



print(a)
