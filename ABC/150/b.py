n = int(input())
S = input()

ans = 0
for i in range(0, n - 2):
    # print(S[i: i + 3])
    if S[i: i + 3] == 'ABC':
        ans += 1
print(ans)
