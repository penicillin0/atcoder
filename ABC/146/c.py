a, b, x = map(int, input().split())

if a + b > x:
    print(0)
    exit()

for i in range(1, 11):
    p = a * (10 ** (i - 1)) + b * (i)
    print(i, p, 10 ** (i - 1))
    # print(p,i)
    if x >= p:
        keta = i
print(keta)
N = (x - b * keta) // a
if N >= 10 ** 9:
    print(10 ** 9)
    exit()
print(N)
