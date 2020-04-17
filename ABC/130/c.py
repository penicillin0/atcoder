W, H, x, y = map(int, input().split())

x0, y0 = W / 2, H / 2
ans = W * H / 2

if (x0, y0) == (x, y):
    print(ans, 1)
else:
    print(ans, 0)
