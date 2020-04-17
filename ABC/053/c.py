x = int(input())
ans = (x // 11) * 2
num = x % 11
if num > 6:
    ans += 2
elif num == 0:
    ans += 0
else:
    ans += 1
print(ans)
