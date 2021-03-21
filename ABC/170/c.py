x, n = map(int, input().split())
P = list(map(int, input().split()))

ans_list = []
min_sa = float('inf')
for i in range(-1, 102):
    if not i in P:
        if min_sa > abs(i - x):
            ans_list = [i]
            min_sa = abs(i - x)
        elif min_sa == abs(i - x):
            ans_list.append(i)
print(min(ans_list))
