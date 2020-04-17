N, L = map(int, input().split())

apple = []
for i in range(1, N+1):
    apple.append(L + i - 1)
apple.sort()


taberu_abs = float('inf')
for a in apple:
    if abs(a) < taberu_abs:
        taberu_abs = abs(a)
        taberu = a

print(sum(apple) - taberu)
