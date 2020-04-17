import bisect
import sys
input = sys.stdin.readline
n = int(input())
L = list(map(int, input().split()))

L.sort()
ans = 0
for i in range(n):
    for j in range(i + 1, n):
        A = L[i] + L[j] - 1
        sa = abs(L[i] - L[j]) + 1
        big = bisect.bisect_right(L, A)
        sml = bisect.bisect_left(L, sa)
        num = big - sml
        if sa <= L[i] <= A:
            num -= 1
        if sa <= L[j] <= A:
            num -= 1
        if num > 0:
            ans += num
print(ans//3)
