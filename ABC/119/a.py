import datetime

a, b, c = map(int, input().split('/'))
d = datetime.date(2019, 4, 30)
f = datetime.date(a, b, c)
if d >= f:
    print('Heisei')
else:
    print('TBD')
