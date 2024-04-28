n, L = map(int, input().split())
p = []

for i in range(n):
    a = [int(i) for i in input().split()]
    p.append((a[0], 1))
    p.append((a[1], -1))

p.sort()

cur = 0
last = 0
ans = 0
for i in p:
    if cur > L:
        ans += (i[0] - last) * (cur - L)
    cur += i[1]
    last = i[0]

print(ans)
