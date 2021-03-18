X = int(input())

num = 100
cnt = 0
for i in range(10 ** 5):
    cnt += 1
    num = int(num * 101)
    num = num // 100
    if X <= num:
        print(cnt)
        exit()
