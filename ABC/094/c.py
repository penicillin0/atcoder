N = int(input())
X = list(map(int, input().split()))
X0 = X[::]
X.sort()
num = int(N / 2 - 1)  # index は num
ans0, ans1 = X[num], X[num + 1]
for i in range(N):
    if X0[i] > ans0:
        print(ans0)
    else:
        print(ans1)
