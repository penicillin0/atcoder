n, k = map(int, input().split())
H = list(map(int, input().split()))

H.sort(reverse=True)
# print(H)
ans = 0

if k >= n:
    print(0)
    exit()

for h in H[k:]:
    ans += h
print(ans)