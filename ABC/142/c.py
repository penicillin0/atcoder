n = int(input())
A = list(map(int, input().split()))
ans = [0] * n
for num, a in enumerate(A):
    ban = a + 1
    ans[ban - 2] = num + 1
ans = list(map(str, ans))
print(' '.join(ans))
