N = int(input())

num = 3505

for i in range(1, num):
    if N / 4 < i:
        for j in range(1, num):
            if N / 4 < (i * j) / (i + j):
                w = (N * i * j) / (4 * i * j - i * N - j * N)
                if w.is_integer():
                    print(i, j, int(w))
                    exit()
