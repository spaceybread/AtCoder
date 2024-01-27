let = 'abcdefghijklmnopqrstuvwxyz'
freq = [0]*26

s = input()

for _ in s:
    char = let.index(_)
    freq[char] += 1
    
m = max(freq)
ind = freq.index(m)

print(let[ind])
