from collections import Counter
N, K = map(int, input().split())
A = list(map(int, input().split()))
C = Counter(A)
D = []
for c in C:
    D.append(C[c])
D.sort(reverse=True)
print(sum(D[K:]))