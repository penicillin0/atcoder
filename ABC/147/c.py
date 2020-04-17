N = int(input())
A = []
XY = []
for i in range(N):
    a = int(input())
    A.append(a)
    XY.append([list(map(int, input().split())) for _ in range(a)])


ans = 0
# print(singi)
for i in range(2 ** N):
    singi = [-1] * (N + 1)
    bin_ = bin(i)[2:].zfill(N)
    flag = True
    for j in range(1, N + 1):
        sin = int(bin_[j - 1])
        person = j
        num = A[j-1]
        questions = XY[j - 1]

        if sin == 0:
            continue

        if singi[j] == -1:
            singi[j] = sin
        else:
            if singi[j] != sin:
                flag = False

        for k in range(num):
            hito, honto = questions[k]
            if singi[hito] == -1:
                singi[hito] = honto
            else:
                if singi[hito] != honto:
                    flag = False

    if flag is True:
        singi = singi[1:]
        for b, s in zip(list(bin_), list(singi)):
            b = int(b)
            s = int(s)
            if (b == 1 and s == 0) or (b == 0 and s==1):
                flag = False
        if flag is True:
            ans = max(ans, singi.count(1))
print(ans)


        



    
