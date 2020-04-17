N = int(input())
S = input()

ans = 0

for i in range(N - 1):
    A = S[:i + 1]
    B = S[i + 1:]
    C = set()
    for a in A:
        if a in list(B):
            C.add(a)
        ans = max(ans, len(C))

print(ans)