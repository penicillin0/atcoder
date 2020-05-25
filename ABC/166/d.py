X = int(input())

a = 2
b = 1

n = int((X ** (1 / 5)) // 1) * 100
# print(n)


for a in range(1, n + 10):
    minus = 1
    b5 = (a ** 5) - X
    if b5 < 0:
        minus = -1
        b5 *= - 1
    b = int(pow(b5, (1 / 5)))
    if (a ** 5 - b ** 5 * minus) == X:
        # print(X)
        print(a, b * minus)
        # print(a, b * minus)
        exit()

