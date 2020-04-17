from fractions import gcd
a, b = map(int, input().split())


def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()
    return divisors


def coprime(a, b):
    return gcd(a, b) == 1


ans = 0
P = make_divisors(a)
Q = make_divisors(b)

kou = list(set(P) & set(Q))
n = len(kou)


ans = []
kou.sort()
for k in kou:
    flag = True
    for i in range(len(ans)):
        if coprime(ans[i], k) is False:
            flag = False
    if flag is True:
        ans.append(k)
print(len(ans))
