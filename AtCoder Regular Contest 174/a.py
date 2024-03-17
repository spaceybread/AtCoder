def maxSubArraySum(a, size):
    max_so_far = -1000000 - 1
    max_ending_here = 0
    l = 0
    r = 0
    s = 0
    
    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here
            l = s
            r = i
                
        if max_ending_here < 0:
            max_ending_here = 0
            s = i + 1
    return [max_so_far, l, r]

def minSubArraySum(a, size):
    max_so_far = 1000000 + 1
    max_ending_here = 0
    l = 0
    r = 0
    s = 0
 
    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        if (max_so_far > max_ending_here):
            max_so_far = max_ending_here
            l = s
            r = i
        if max_ending_here > 0:
            max_ending_here = 0
            s = i + 1
    return [max_so_far, l, r]

n, c = map(int, input().split())
a = list(map(int, input().split()))
    
maxout = maxSubArraySum(a, n)
minout =  minSubArraySum(a, n)

maxsum = 0
minsum = 0
normal = 0

for i in range(n):
    if i >= maxout[1] and i <= maxout[2]:
        #print(a[i])
        maxsum += c*a[i]
    else:
        #print(a[i])
        maxsum += a[i]
    if i >= minout[1] and i <= minout[2]:
        minsum += c*a[i]
    else:
        minsum += a[i]
    normal += a[i]

print(max([maxsum, minsum, normal]))
