S = input()

AA = S[:2]
BB = S[2:]
a = []
for i in range(1, 13):
    if 1 <= i <= 9:
        a.append('0' + str(i))
    else:
        a.append(str(i))
if not AA in a and not BB in a:
    print('NA')
elif AA in a and BB in a:
    print('AMBIGUOUS')
elif AA in a:
    print('MMYY')
else:
    print('YYMM')