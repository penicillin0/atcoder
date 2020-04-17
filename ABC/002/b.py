W = input()
ans = ''
for w in W:
    if w not in ['a', 'i', 'u', 'e', 'o']:
        ans += w
print(ans)
