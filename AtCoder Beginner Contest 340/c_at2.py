# i thought i had a creative solution, turns out it was not a solution

# as per this comment: https://www.youtube.com/watch?v=jMu_1zzJESA&lc=Ugzn0D5L8sSTVYaeKpV4AaABAg.A-dKD8UkzULA-dMIpUNJco, it's because floating point numbers weren't sufficient for this constraint 

import math
n = int(input())
val = math.floor(math.log2(n))
wo1 = val * n
add = (n - 2**val) * 2
print(wo1 + add)

