import os

contest_num = input('input ABC<contest number> => ')

problem_6 = ['a', 'b', 'c', 'd', 'e', 'f']
problem_4 = ['a', 'b', 'c', 'd']

if int(contest_num) > 125:
    problem = problem_6
else:
    problem = problem_4


if len(contest_num) == 0:
    print('Try again. Input format was bad.')
    exit()

make_or_not = 'y'
make_or_not = input('make ABC' + contest_num + '?(y/n)')
if make_or_not != 'y':
    print('accept your reject this process')
    exit()

# ディレクトリが無ければ作る
if not os.path.exists('./' + contest_num):
    os.mkdir('./' + contest_num)


for p in problem:
    # あったらpass
    if os.path.exists('./' + contest_num + '/' + p + '.py'):
        continue

    f = open('./' + contest_num + '/' + p + '.py', 'w')
print('complete!')
