S = input()
T = input()

moji = ['a', 't', 'c', 'o', 'd', 'e', 'r']

for s, t in zip(S, T):
    if s == t:
        continue
    else:
        if (s == '@' and t in moji) or (t == '@' and s in moji):
            continue
        else:
            print('You will lose')
            exit()

print('You can win')
