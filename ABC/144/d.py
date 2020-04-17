from math import atan
from math import pi

a, b, x = map(int, input().split())

if a * a * b / 2 <= x:
    ans = atan((2 * b) / a - 2 * x / (a ** 3))
    ans = ans * 180 / pi
else:
    ans = atan(2 * x / (a * (b ** (2))))
    ans = ans * 180 / pi
    ans = 90 - ans
print(ans)
