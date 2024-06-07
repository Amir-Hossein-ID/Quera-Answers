import math

t = int(input())

for i in range(t):
    n = int(input())
    curd = max(n - 2, 0)
    ans = (curd + 2) * (curd) + 1
    last = (curd) * 2 - 1
    ans += (last + (last % 6)) * math.ceil(last / 6)  // 2
    print(ans)
