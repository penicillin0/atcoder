n, k = map(int, input().split())
A = list(map(int, input().split()))
A.sort(reverse=True)

mod = 10**9+7
fact, fact_inv = [1], [1]
for i in range():  # change here
    new_fact = fact[-1] * (i+1) % mod
    fact.append(new_fact)
    fact_inv.append(pow(new_fact, mod-2, mod))


def mod_comb_k(n, k, mod):
    return fact[n] * fact_inv[k] % mod * fact_inv[n-k] % mod























# dp = [0] * (n + 1)




# for i in range(n + 1):
#     m = n - i
#     if m >= k:


