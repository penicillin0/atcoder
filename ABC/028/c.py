ABC = list(map(int, input().split()))

sm = set()
for i in range(5):
    for j in range(i + 1, 5):
        for k in range(j + 1, 5):
            sm.add(ABC[i] + ABC[j] + ABC[k])
sm = list(sm)
sm.sort()
print(sm[-3])