a, b = input().split()
c = int(a + b)
d = (c**(1 / 2)) // 1
print('Yes' if d**2 == c else 'No')
