n, k = (map(int, input().split()))
a = list(map(int, input().split()))

sum = (k * (k + 1))
sum = sum >> 1

dict = {}

for s in a:
    if s < k + 1:
        if dict.get(s) == None:
            sum -= s
            dict[s] = True

print(sum)
