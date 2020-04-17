a, b, x = map(int, input().split())

if a + b > x:
    print(0)
    exit()

if a * (10 ** 9) + b * 9 <= x:
    print(1000000000)
    exit()

keta = 1
for i in range(1, 10):
    p = a * (10 ** i) + b * (i + 1)
    if p <= x:
        keta = i + 1
    else:
        break


N = (x - b * keta) // a
print(N)
