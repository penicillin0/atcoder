n = int(input())
A = list(map(int, input().split()))

buka_info = dict()

for i, a in enumerate(A):
    num = i + 2
    if a in buka_info:
        buka_info[a].append(num)
    else:
        buka_info[a] = [num]

for i in range(1, n + 1):
    if i not in buka_info:
        print(0)
    else:
        print(len(buka_info[i]))
