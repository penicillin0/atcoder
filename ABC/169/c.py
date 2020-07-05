from decimal import Decimal
a, b = map(str, input().split())
ans = Decimal(a) * Decimal(b)
print(int(ans))
