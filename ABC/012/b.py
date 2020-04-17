n = int(input())

a = n // 3600
b = (n - 3600 * a) // 60
c = n - 3600 * a - 60 * b
print(str(a).zfill(2) + ':' + str(b).zfill(2) + ':' + str(c).zfill(2))
