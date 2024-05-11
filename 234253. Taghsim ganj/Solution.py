t = int(input())

for _ in range(t):
    n, m, k = map(int, input().split())
    g = [[int(i) for i in input().split()] for j in range(k)]
    if k % 4 != 0:
        print('NO')
        continue
    g.sort()
    ii = k//2
    if g[ii][0] == g[ii-1][0]:
        print('NO')
        continue
    ii = g[ii-1][0]
    a = [p[1] for p in g if p[0]<=ii]
    b = [p[1] for p in g if p[0]>ii]
    a.sort()
    b.sort()
    jj = (k//2)//2
    if a[jj] == a[jj-1]:
        print('NO')
        continue
    if b[jj] == b[jj-1]:
        print('NO')
        continue
    if a[jj-1] >= b[jj]:
        print('NO')
        continue
    if a[jj] <= b[jj-1]:
        print('NO') 
        continue
    print('YES')
