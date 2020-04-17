N = int(input())
A = list(map(int, input().split()))
ans = []
for i in range(N):  # 高橋くん
    Aokimax = [-float('inf'), -float('inf')]
    for j in range(N):  # 青木くん
        Tak, Aok = 0, 0
        if i > j:
            nums = A[j:i + 1]
        elif i < j:
            nums = A[i:j + 1]
        else:
            continue

        for k in range(len(nums)):
            if (k + 1) % 2 == 1:
                Tak += nums[k]
            else:
                Aok += nums[k]
        if Aokimax[0] < Aok:
            Aokimax[0] = Aok
            Aokimax[1] = Tak
    ans.append(Aokimax[1])
print(max(ans))
