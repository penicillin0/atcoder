x = int(input())


if x == 2:
    print(2)
    exit()


def sosu(n):
    m = int(n ** (1 / 2) + 1)
    flag = True
    for i in range(2, m + 1):
        if n % i == 0:
            flag = False
    return flag


for i in range(10 ** 6):
    if sosu(x + i):
        print(x + i)
        exit()

