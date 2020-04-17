n = int(input())

a = 0
b = 0
c = 1
q = 10007

if n == 1:
    print(a)
    exit()
elif n == 2:
    print(b)
    exit()
elif n == 3:
    print(c)
    exit()


for i in range(n - 3):
    d = a + b + c
    a = b
    b = c
    c = d
    c %= q

print(c)
