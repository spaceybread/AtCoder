# i thought i had a creative solution, turns out it was not a solution

import math
n = int(input())
val = math.floor(math.log2(n))
wo1 = val * n
add = (n - 2**val) * 2
print(wo1 + add)

