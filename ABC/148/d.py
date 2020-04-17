n = int(input())
A = list(map(int, input().split()))

num = 1
ans = 0

if 1 not in A:
    print(-1)
    exit()

for i in range(n):
    a = A[i]
    if a == num:
        num += 1
        continue
    else:
        ans += 1
print(ans)
