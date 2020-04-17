n = int(input())
m = len(str(n))
ans = 0



for i in range(n + 1):
    A = str(i)
    first = A[0]
    end = A[-1]

    if end == '0':
        continue
    if first == end:
        ans += 1


    if m >= 3:
        for j in range(m - 2):
            ans += 10 ** (j)
    mini = int(end + '0' * (m - 2) + first)
    maxi = int(end + '9' * (m - 2) + first)
    # print(mini, maxi)
    if n < mini:
        continue
    elif mini <= n <= maxi:
        # print(i, mini, maxi)
        if int(str(n)[-1]) >= int(first):
            ans += int(str(n)[1:-1]) + 1
            # print('a')
        else:
            ans += int(str(n)[1:-1])
            # print('a')
    else:
        ans += (10 ** (m - 2))

print(ans)
