from math import ceil
A, B, C = map(int, input().split())
ABC = [A, B, C]
big = max(ABC)
smal = min(ABC)
mid = sum(ABC) - big - smal

ans = big - mid
smal += ans
if (big - smal) % 2 == 0:
    ans += (big - smal) / 2
else:
    ans += (big - smal) / 2 + 1.5
print(int(ans))
