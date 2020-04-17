from copy import deepcopy
N, K = map(int, input().split())
S = list(input())
sort_S = list(sorted(S))

# ここがちがう


def list_dif(listA, listB):
    rep = 0
    list_cnt = list(set(listA))
    for a in list_cnt:
        rep += min(listA.count(a), listB.count(a))
    return len(listA) - rep


def list_dif_order(listA, listB):
    rep = 0
    for i in range(len(listA)):
        if listA[i] != listB[i]:
            rep += 1
    return rep


ans = []
for i in range(N):
    for j in range(len(sort_S)):
        kouho = sort_S[j]
        mae = ans + [sort_S[j]]
        sort_SS = deepcopy(sort_S)
        sort_SS.pop(j)
        ushiro = sort_SS
        if K >= list_dif_order(mae, S[:i+1]) + list_dif(ushiro, S[i+1:]):
            ans.append(kouho)
            sort_S.pop(j)
            break


print(''.join(ans))
