#DICTS OF COURSE

n = int(input())
a = list(map(int, input().split()))

index_dict = {val: i + 1 for i, val in enumerate(a)}
ord_list = [index_dict[-1]]

for i in range(n - 1):
    ln = index_dict[ord_list[i]]
    ord_list.append(ln)

print(*ord_list, sep=" ")
