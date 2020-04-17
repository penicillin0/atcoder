n = int(input())
goal_nums = list(map(int, (input().split())))

ans_nums = [0] * n
start_i = 0
goal_i = 0
count = 0

while goal_nums != ans_nums:
    # 水のあげ始めを決定
    for i in range(n):
        if goal_nums[i] != ans_nums[i]:
            start_i = i
            break
    # 水のあげ終わりを決定
    for j in range(start_i, n):
        if goal_nums[j] == ans_nums[j]:
            goal_i = j
            break
        if j == n - 1:
            goal_i = n

    # 指定箇所に水を上げる
    for k in range(start_i, goal_i):
        ans_nums[k] += 1
    count += 1

print(count)
