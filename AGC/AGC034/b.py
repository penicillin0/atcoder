from collections import deque
S = list(input())
N = len(S)
S = deque(S)


def solve(L):
    if 'BC' not in ''.join(L):
        return 0
    while L[-1] == 'A':
        L.pop()
    A_place = []
    n = len(L) - 1
    for i in range(n):
        if L[i] == 'A':
            A_place.append(i)
    a = len(A_place)
    return int(((a * n - sum(A_place)) - (a * (a - 1) / 2)) / 2)


ans = 0
part_S = []
num = 0
while S:
    if part_S == []:
        if S[0] == 'A':
            part_S.append('A')
            S.popleft()
        else:
            S.popleft()
    else:
        if len(S) >= 2:
            if S[0] == 'A':
                part_S.append('A')
                S.popleft()
            elif S[0] + S[1] == 'BC':
                part_S.append('B')
                part_S.append('C')
                S.popleft()
                S.popleft()
            else:
                ans += solve(part_S)
                S.popleft()
                part_S = []
        else:
            break
ans += solve(part_S)
print(ans)
