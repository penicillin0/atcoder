N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = 0
for i in range(N):
    if A[i] >= B[i]:
        ans += B[i]
        A[i] -= B[i]
    else:
        ans += A[i]
        yoryoku = B[i] - A[i]
        A[i] = 0
        if A[i + 1] >= yoryoku:
            ans += yoryoku
            A[i+1] -= yoryoku
        else:
            ans += A[i+1]
            A[i + 1] = 0
print(ans)
