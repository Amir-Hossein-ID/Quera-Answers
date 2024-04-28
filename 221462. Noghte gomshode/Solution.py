fs = []
ss = []
ts = []
for i in range(7):
    x,y,z =map(int,input().split())
    fs.append(x)
    ss.append(y)
    ts.append(z)
ans = []
for i in fs:
    if fs.count(i) == 3:
        ans.append(i)
        break
for i in ss:
    if ss.count(i) == 3:
        ans.append(i)
        break
for i in ts:
    if ts.count(i) == 3:
        ans.append(i)
        break
print(*ans)
