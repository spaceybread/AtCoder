b = int(input())

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
prods = []

for i in nums:
    prods.append(i**i)

#print(prods)

if (b in prods):
    a = prods.index(b)
    print(nums[a])
else:
    print(-1)

