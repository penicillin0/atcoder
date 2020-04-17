S = int(input())
x0, y0 = 0, 0
n = pow(S, 1 / 2) + 1
n = int(n)
x1, y2 = n, n
x2 = n ** 2 - S
y1 = 1
num = 10 ** 9
if x1 <= num and y1 <= num and x2 <= num and y2 <= num:
    print(x0, y0, x1, x2, y1, y2)
else:
    x0, y0 = 0, 0
    n = 10 ** 9
    x1, y2 = n, n
    x2 = n ** 2 - S
    y1 = 1
    print(x0, y0, x1, x2, y1, y2)
