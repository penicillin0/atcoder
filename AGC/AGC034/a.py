N, A, B, C, D = map(int, input().split())
S = input()
S = 'S' + S

if C < D:
    if '##' not in S[A:D + 1]:
        print('Yes')
    else:
        print('No')
else:
    if '...' in S[B - 1:D + 2]:
        if '##' not in S[A:C]:
            print('Yes')
        else:
            print('No')
    else:
        print('No')
