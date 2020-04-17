N, Q = map(int, input().split())
s = input()
TD = [input().split() for _ in range(Q)]

ss = list(set(s))
ss_count = {}

for i in range(N):
    string = s[i]
    if string in ss_count:
        ss_count[string] += 1
    else:
        ss_count[string] = 1

print(ss_count)
