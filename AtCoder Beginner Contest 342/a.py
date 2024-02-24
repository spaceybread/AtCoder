s = input()

let = []
ct = []

for i in range(len(s)):
    if s[i] not in let:
        let.append(s[i])
        
let_0_start = s.index(let[0])
let_1_start = s.index(let[1])
let_0_end = len(s) - s[::-1].index(let[0]) - 1
let_1_end = len(s) - s[::-1].index(let[1]) - 1

#print(let_0_start, let_0_end, let_1_start, let_1_end)

if let_0_start == let_0_end:
    print(s.index(let[0]) + 1)
else:
    print(s.index(let[1]) + 1)
