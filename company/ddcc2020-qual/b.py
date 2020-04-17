N = int(input())
A = list(map(int, input().split()))

ans = float('inf')
left = 0
right = 0
allA = sum(A)


for i in range(N):
    left += A[i]
    right = allA - left
    ans = min(ans, abs(right - left))
print(ans)


