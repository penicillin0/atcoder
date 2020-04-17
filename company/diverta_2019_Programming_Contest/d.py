N = int(input())

M = int((N + 1)**(1 / 2))
ans = 0
for i in range(1, M):
    if (N - i) % i == 0:
        ans += ((N - 1) // i)
print(ans)
