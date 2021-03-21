import math
A, B = map(int, input().split())

all_a_b = []

for i in range(2000):
    a_ = math.floor(i * 0.08)
    b_ = math.floor(i * 0.1)
    all_a_b.append((i, a_, b_))

ans = float('inf')
for i, a, b in all_a_b:
    if a == A and b == B:
        ans = min(ans, i)
if ans == float('inf'):
    print(-1)
else:
    print(ans)
