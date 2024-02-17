def gcd3(a, b):
    if (b == 0):
        return abs(a)
    else:
        return gcd3(b, a % b)
        
def lcm3(a, b):
    return int((abs(a * b))/(gcd3(a, b)))

a = list(map(int, input().split()))
n = a[0]
m = a[1]
k = a[2]

l = lcm3(n, m)

if l != n and l != m:
    n_l = int(l / n) - 1
    m_l = int(l / m) - 1

    j = n_l + m_l

    #print(n_l, m_l)

#print(k / j, k % j)

    k_j = int((k - (k % j)) / j)

    #print(k_j, k % j)

    base = k_j * l

    sols = []
    
    n_r = 0
    m_r = 0
    for i in range(1, 2 * (k % j)):
        
        if base + (n * (n_r + 1)) < base + (m * (m_r + 1)):
            n_r += 1
            sols.append(base + n * n_r)
        else:
            m_r += 1
            sols.append(base + m * m_r)
    #print(sols)
    print(sols[k % j - 1])

else:
    j = n
    t = m
    if l != n:
        j = m
        t = n
        
    print(j * k - t)
