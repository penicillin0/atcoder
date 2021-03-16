n, m = map(int, input().split())
A = list(map(int, input().split()))
cnt = 0

all_point = sum(A)
border = all_point / (4*m)
for a in A:
    if a >= border:
        cnt += 1
if cnt >= m:
    print('Yes')
else:
    print('No')
