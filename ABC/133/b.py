N, D = map(int, input().split())
XD = [list(map(int, input().split())) for _ in range(N)]

ans = 0


def dist(list1, list2):
    rep = 0
    for k in range(len(list1)):
        rep += (list1[k] - list2[k])**2
    return rep**(1 / 2)


for i in range(N):
    xd1 = XD[i]
    for j in range(i + 1, N):
        xd2 = XD[j]
        if dist(xd1, xd2) == int(dist(xd1, xd2)):
            ans += 1
print(ans)
