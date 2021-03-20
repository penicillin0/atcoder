n = int(input())
A = list(map(int, input().split()))

set_a = set()
for a in A:
    if a in set_a:
        print("NO")
        exit()
    set_a.add(a)
print("YES")
