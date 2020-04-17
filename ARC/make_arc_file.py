import os

contest_num = input('input ARC<contest number> => ')

if len(contest_num) == 0:
    print('Try again. Input format was bad.')
    exit()

make_or_not = 'y'
make_or_not = input('make ARC' + contest_num + '?(y/n)')
if make_or_not != 'y':
    print('reject process')
    exit()

if os.path.exists('./ARC' + contest_num):
    print('already maked ARC' + contest_num)
    exit()

problem = ['a', 'b', 'c', 'd']
os.mkdir('./ARC' + contest_num)
for p in problem:
    f = open('./ARC' + contest_num + '/' + p + '.py', 'w')
print('complete!')
