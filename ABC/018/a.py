a = int(input())
b = int(input())
c = int(input())
d = [a, b, c]
aa, bb, cc = 0, 0, 0

if a == max(d):
    aa = 1
if b == max(d):
    bb = 1
if c == max(d):
    cc = 1
if a == min(d):
    aa = 3
if b == min(d):
    bb = 3
if c == min(d):
    cc = 3

for e in [aa, bb, cc]:
    if e == 0:
        print(2)
    else:
        print(e)
