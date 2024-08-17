n, k = map(int, input().split())
x = list(map(int, input().split()))
a = list(map(int, input().split()))

def f(x, p):
    if p == 0:
        return [i for i in range(n)]
    elif p % 2 == 0:
        y = f(x, p // 2)
        return [y[v] for v in y]
    else:
        y = f(x, p - 1)
        return [y[v] for v in x]


x = f([v - 1 for v in x], k)

print(*[a[v] for v in x])
