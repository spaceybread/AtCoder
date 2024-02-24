#im really upset about this one, it was so close to being within the time limit 2223 vs the limit of 2000

n = int(input())
s = input()
q = int(input())

# record start time

pos = {char: [] for char in "abcdefghijklmnopqrstuvwxyz"}

for i in range(n):
    id = s[i]
    pos[id].append(i)

for _ in range(q):
    ln = input().split()
    if ln[0] != ln[1]:
        c_id = ln[0]
        d_id = ln[1]

        pos[d_id].extend(pos[c_id])
        pos[c_id] = []

out = [0] * n

for char, indices in pos.items():
    for idx in indices:
        out[idx] = char

print("".join(out))

