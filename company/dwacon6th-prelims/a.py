n = int(input())
ST = [list(map(str, input().split())) for _ in range(n)]
X = input()

ans = 0
flag = False
for st in ST:
    a, b = st
    b = int(b)
    if X == a:
        flag = True
        continue
    
    if flag is True:
        ans += b
print(ans)