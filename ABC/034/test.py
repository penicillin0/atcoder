from time import time


def pow_s(x, n):
    ret = 1
    for i in range(1, n + 1):
        ret *= i
    return ret


def pow_f(x, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return pow_f(x**2, n // 2)
    else:
        return x * pow_f(x**2, (n - 1) // 2)


n = int(input())
s0 = time()
c = pow_s(n, n)
e0 = time()

s1 = time()
a = pow(n, n)
e1 = time()

s2 = time()
b = pow_f(n, n)
e2 = time()

print('slow(for文):       ' + str(e0 - s0))
print('組み込み関数(pow): ' + str(e1 - s1))
print('fast(再帰O(lon n)):' + str(e2 - s2))
