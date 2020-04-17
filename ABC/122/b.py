S = input()
S = S.replace('A', '*').replace('T', '*').replace('C', '*').replace('G', '*')

ans, count = 0, 0
for s in S:
    if s == '*':
        count += 1
        ans = max(ans, count)
    else:
        count = 0

print(ans)
