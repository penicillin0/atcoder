N = int(input())
S = []
A, B, AB, BA = 0, 0, 0, 0
for i in range(N):
    a = input()
    S.append(a)
    if a[0] == 'B' and a[-1] == 'A':
        BA += 1
    elif a[0] == 'B':
        B += 1
    elif a[-1] == 'A':
        A += 1
    AB += a.count('AB')
ans = 0

ans += AB + min(A, B)
ans += BA
if A == 0 and B == 0 and BA > 0:
    ans -= 1
print(ans)