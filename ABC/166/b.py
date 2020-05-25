n, k = map(int, input().split())


cnt = [0] * n
for i in range(k):
    d = input()
    A = map(int, input().split())
    for a in A:
        a -= 1
        cnt[a] += 1
print(cnt.count(0))
