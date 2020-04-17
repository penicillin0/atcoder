N = int(input())
L = []

for i in range(1, 10):
    for j in range(1, 10):
        L.append(i * j)
if N in L:
    print('Yes')
else:
    print('No')
