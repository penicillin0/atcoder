N = int(input())
H = list(map(int, input().split()))

now = H[0] - 1
H[0] = H[0] - 1

for i in range(1, N):
    if H[i] > now:
        H[i] -= 1
    now = H[i]


for i in range(N - 1):
    if H[i + 1] >= H[i]:
        continue
    else:
        print('No')
        exit()
print('Yes')
