N, X = map(int, input().split())
VP = [list(map(int, input().split())) for _ in range(N)]

alc = 0
X *= 100
cnt = 0
# if
for v, p in VP:
    this_alc = v * p
    alc += this_alc
    cnt += 1
    if alc > X:
        print(cnt)
        exit()
print(-1)
