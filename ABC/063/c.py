N = int(input())
S = [int(input()) for _ in range(N)]

S.sort()
ans = sum(S)
if ans % 10 != 0:
    print(ans)
    exit()

for i in range(N):
    if (ans - S[i]) % 10 != 0:
        print(ans - S[i])
        exit()
print(0)
