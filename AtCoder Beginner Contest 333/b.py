def findL(points):
    pent = ["A", "B", "C", "D", "E"]

    diff = pentagon.index(points[1]) - pentagon.index(points[0])
    if 5 - diff < diff:
        diff = 5 - diff
    return diff

pentagon = ["A", "B", "C", "D", "E"]

ln1 = input()

if pentagon.index(ln1[1]) < pentagon.index(ln1[0]):
    ln1 = ln1[1] + ln1[0] 

ln2 = input()

if pentagon.index(ln2[1]) < pentagon.index(ln2[0]):
    ln2 = ln2[1] + ln2[0] 

#print(findL(ln1))
#print(findL(ln2))
if findL(ln1) == findL(ln2):
    print("Yes")
else:
    print("No")
