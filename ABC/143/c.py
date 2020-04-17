n = int(input())
S = list(input())

ans = 0

b = S[0]
for i in range(1, n):
    if S[i] != b:
        ans += 1
        b = S[i]
    else:
        continue
print(ans + 1)
