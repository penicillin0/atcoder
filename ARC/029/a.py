N = int(input())
T = []
for i in range(N):
    T.append(int(input()))

mini = float('inf')
for b in range(2**N):
    right, left = 0, 0
    for k in range(N):
        if b & (1 << k):
            right += T[k]
        else:
            left += T[k]
    if mini > abs(right - left):
        mini = abs(right - left)
        mini_time = max(right, left)
print(mini_time)
