S = list(input())
SS = S[::-1]
cnt =0
for i in range(len(S)):
    if S[i] != SS[i]:
        cnt += 1
print(cnt//2)