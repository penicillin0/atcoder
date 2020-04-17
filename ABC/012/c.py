N = int(input())
num = 2025 - N
for i in range(1, 10):
    for j in range(1, 10):
        if i * j == num:
            print(str(i) + ' x ' + str(j))
