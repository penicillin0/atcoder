H, W = map(int, input().split())

if H % 3 == 0 or W % 3 == 0:
    print(0)
    exit()

ans = float('inf')
a, b, c, d = 0, 0, 0, 0

if H % 2 == 0:
    c, d = H / 2, H / 2
else:
    c, d = H // 2, H // 2 + 1

for i in range(-2, 3):
    a = W // 3 + i
    b = W - a
    if a > 0 and b > 0:
        pqr = [a * H, b * c, b * d]
        ans = min(ans, max(pqr) - min(pqr))
ans = min(ans, H)
H, W = W, H

if H % 2 == 0:
    c, d = H / 2, H / 2
else:
    c, d = H // 2, H // 2 + 1

for i in range(-2, 3):
    a = W // 3 + i
    b = W - a
    if a > 0 and b > 0:
        pqr = [a * H, b * c, b * d]
        ans = min(ans, max(pqr) - min(pqr))
ans = min(ans, H)
print(int(ans))
