X = input()

replace_list = ['o', 'u', 'k', 'ch']

for r in replace_list:
    X = X.replace(r, '')
if X == '':
    print('YES')
else:
    print('NO')
