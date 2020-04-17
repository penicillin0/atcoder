N = int(input()) % 30

s = list(range(1, 7))
for i in range(N):
    a = i % 5
    b = a + 1
    s[a], s[b] = s[b], s[a]
print(''.join(list(map(str, s))))
