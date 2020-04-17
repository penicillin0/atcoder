N = int(input())
A = list(map(int, input().split()))


def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    return divisors


num = int(N // 2 + 1)
cnt = {}
for i in range(1, N + 1):
    cnt[i] = 0
A.reverse()
B = []

for i, a in enumerate(A):
    i = N - i
    if i >= num:
        if a == 1:
            for p in make_divisors(i):
                cnt[p] = (cnt[p] + 1) % 2
            B.append(i)
    else:
        if cnt[i] != a:
            for p in make_divisors(i):
                cnt[p] = (cnt[p] + 1) % 2
            B.append(i)

print(len(B))
B = list(map(str, B))
print(' '.join(B))
