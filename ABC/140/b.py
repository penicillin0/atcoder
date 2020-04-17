n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

ans = 0
mae = -1
for i in range(n):
    a = A[i]
    ans += B[a-1]
    if a - 1 == mae:
        ans += C[mae-1]
    mae = a
print(ans)
