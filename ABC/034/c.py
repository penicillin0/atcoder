m = 1000000007
W, H = map(int, input().split())


def f(n):
    ret = 1
    for i in range(1, n + 1):
        ret = i * ret % m
    return ret


def pow_r(x, n, p):
    """
    O(log n)
    """
    if n == 0:  # exit case
        return 1
    if n % 2 == 0:  # standard case ① n is even
        return pow_r(x**2 % p, n // 2, p)
    else:  # standard case ② n is odd
        return x * pow_r(x**2, (n - 1) // 2, p) % p


print(f(W + H - 2) * pow_r(f(H - 1), m - 2, m) * pow_r(f(W - 1), m - 2, m) % m)
