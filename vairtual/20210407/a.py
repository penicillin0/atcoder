import math
n, d = map(int, input().split())
cnt = 1 + 2 * d

print(math.ceil(n / cnt))
