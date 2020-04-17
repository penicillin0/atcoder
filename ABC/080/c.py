N = int(input())
A = list(map(int, input().split()))
two, four = 0, 0
for a in A:
    if a % 4 == 0:
        four += 1
    elif a % 2 == 0:
        two += 1
if two == 0:
    can = four * 2 + 1
else:
    can = four * 2 + two

if can >= N:
    print('Yes')
else:
    print('No')