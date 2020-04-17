N = int(input())
S = [''.join(list(sorted(list(input())))) for _ in range(N)]
ans = 0


def nC2(num):
    return int(num * (num - 1) / 2)


count_dict = {}

for s in S:
    if s in count_dict:
        count_dict[s] += 1
    else:
        count_dict[s] = 1

L = list(count_dict.values())

for l in L:
    ans += nC2(l)
print(ans)
