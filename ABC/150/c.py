import itertools
n = int(input())
L = list(range(1, n + 1))
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))
junretu = list(itertools.permutations(L))
junretu.sort()
a, b = 0, 0
for i, jun in enumerate(junretu):
    if P == jun:
        a = i
    if Q == jun:
        b = i
print(abs(a-b))