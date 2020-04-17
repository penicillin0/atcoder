N = int(input())
A = list(map(int, input().split()))
q = 10 ** 9 + 7
ans = 0
cnt = [0] * 61
for i in range(N):
    b = bin(A[i])[2:].zfill(61)
    for i in range(61):
        if b[i] == '1':
            cnt[i] += 1
for num, c in enumerate(cnt[::-1]):
    zero = N - c
    ichi = c
    ans += zero * ichi * (2 ** num)
    ans = ans % q
print(ans)
