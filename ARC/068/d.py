from collections import Counter
N = int(input())
A = list(map(int, input().split()))

count_A = Counter(A)
# print(count_A)

gusu = 0
for a in count_A:
    if count_A[a] % 2 == 0:
        gusu += 1
print(len(count_A) - gusu % 2)