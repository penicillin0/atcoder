a = input()
b = input()

if len(a) > len(b):
    a, b = b, a
print(b)