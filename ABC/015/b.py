import math
n = int(input())
A = list(map(int, input().split()))

cnt = 0
bug_num = 0
for a in A:
    if a == 0:
        continue

    cnt += 1
    bug_num += a
print(math.ceil(bug_num/cnt))
