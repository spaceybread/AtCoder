# editorial solution, @cache memoises a recursive function? I had no idea. Cool trick tho

from functools import cache

@cache
def f(N):
    return 0 if N == 1 else f(N // 2) + f((N + 1) // 2) + N

print(f(int(input())))
