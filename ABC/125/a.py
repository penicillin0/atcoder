A, B, T = map(int, input().split())

ans = 0
time = 0
for i in range(1, 22):
    time += A
    if time > T:
        break
    ans += B

print(ans)