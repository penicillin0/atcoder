S, T = input(), input()
if len(T) > len(S):
    print('UNRESTORABLE')
    exit()

able_list = []

for i in range(len(S) - len(T) + 1):
    S_part = S[i:len(T) + i]
    for j in range(len(T)):
        if S_part[j] == T[j] or S_part[j] == '?':
            if j == len(T) - 1:
                able_list.append(S[0:i] + T + S[len(T) + i:])
            continue
        else:
            break

if not able_list:
    print('UNRESTORABLE')
    exit()

for i in range(len(able_list)):
    able_list[i] = able_list[i].replace('?', 'a')

able_list.sort()
print(able_list[0])