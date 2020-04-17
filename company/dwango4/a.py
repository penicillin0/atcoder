s = list(input())
n = len(s)

two, five = 0, 0
for a in s:
    if a == '2':
        two += 1
    else:
        five += 1
    if two < five:
        print(-1)
        exit()

if s.count('2') != s.count('5'):
    print(-1)
    exit()

count, ans = 0, 0
for a in s:
    if a == '2':
        count += 1
    else:
        count -= 1
    ans = max(ans, count)

print(ans)
