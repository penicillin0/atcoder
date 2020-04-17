n = int(input())
D = list(map(int, input().split()))
D.sort()
n1 = n // 2
n0 = n1 - 1

if D[n0] == D[n1]:
    print(0)
else:
    print(-(D[n0] - D[n1]))
