import sys
input = sys.stdin.readline
R, G, B, N = map(int, input().split())

r, g, b = int(N // R), int(N // G), int(N // B)

ans = 0
for i in range(r + 1):
    if i * R > N:
        break
    for j in range(g + 1):
        if (N - (i * R + j * G)) % B == 0 and (N - (i * R + j * G)) >= 0:
            ans += 1
print(ans)
