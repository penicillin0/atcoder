N = int(input())


def so_bunkai(num, dicts):
    N = num
    num = int(num**(1 / 2) // 1)
    for i in range(2, num + 2):
        while N % i == 0:
            N /= i
            if i in dicts:
                dicts[i] += 1
            else:
                dicts[i] = 1
    if N != 1:
        if N in dicts:
            dicts[int(N)] += 1
        else:
            dicts[int(N)] = 1
    return dicts


ans_dict = {}
for i in range(1, N + 1):
    ans_dict = so_bunkai(i, ans_dict)

asd = 10**9 + 7
ans = 1
for d in ans_dict:
    ans *= (ans_dict[d] + 1)
    ans %= asd

print(ans)
