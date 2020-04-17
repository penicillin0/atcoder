N = int(input())
S = list(input())

w_cnt = [0]
w = 0
for s in S:
    if s == '.':
        w += 1
    w_cnt.append(w)

b_cnt = [0]
b = 0
for s in S[::-1]:
    if s == '#':
        b += 1
    b_cnt.append(b)


ans = float('inf')
i = 0
for b, w in zip(b_cnt[::-1], w_cnt):
    ww, bb = i, N - i
    ans = min(ans, abs(b - bb) + abs(w - ww))
    i += 1
print(ans)
