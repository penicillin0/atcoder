N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]
S = []
for i in range(N):
    S.append(set())

for ab in AB:
    a, b = ab
    a, b = a - 1, b - 1
    S[a].add(b)
    S[b].add(a)

for num, s in enumerate(S):
    myfrd = S[num]
    myfrd.add(num)
    frd = set()
    for f in s:
        frd = frd | S[f]
    print(len(frd - myfrd))
