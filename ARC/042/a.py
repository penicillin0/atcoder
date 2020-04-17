n, m, *a = map(int, open(0).read().split())
q=[[m-i,i+1] for i in range(n)]
for i in range(m):
    q[a[i]-1][0]=m+1+i
q.sort(key=lambda x: x[0])
for p in q[::-1]:
    print(p[1])
