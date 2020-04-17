n = int(input())

str_n = str(n)
m = len(str_n)

ans = 0


for i in range(m):
    keta = m - i
    num = int(str_n[i])
    if num >= 5:
        ans += 1
    
    if i == 0:
        ans += num * keta
    
        
    
