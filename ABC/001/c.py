xa, ya, xb, yb, xc, yc = map(int, input().split())
xb, yb = xb - xa, yb - ya
xc, yc = xc - xa, yc - ya
print(1 / 2 * abs(xb * yc - xc * yb))
