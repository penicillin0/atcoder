a = int(input())
b = int(input())

if a / b == a // b:
    per_num = a // b
else:
    per_num = a // b + 1

print(per_num * b - a)
