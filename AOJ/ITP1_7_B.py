ans_list = []
while True:
    ans = 0
    n, x = map(int, input().split())
    if n == x == 0:
        for a in ans_list:
            print(a)
        exit()
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            k = x - i - j
            if i < j < k <= n:
                ans += 1
    ans_list.append(ans)