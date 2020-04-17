N = int(input())
A = list(map(int, input().split()))
cnt = [0] * (max(A) + 2)


for a in A:
    if a != 0:
        cnt[a - 1] += 1
    cnt[a] += 1
    cnt[a+1] += 1

cnt.sort(reverse=True)
print(cnt[0])
