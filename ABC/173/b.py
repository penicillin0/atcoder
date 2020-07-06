from collections import Counter

n = int(input())
S = [input() for _ in range(n)]
S_cnt = Counter(S)

print('AC x ' + str(S_cnt['AC']))
print('WA x ' + str(S_cnt['WA']))
print('TLE x ' + str(S_cnt['TLE']))
print('RE x ' + str(S_cnt['RE']))
