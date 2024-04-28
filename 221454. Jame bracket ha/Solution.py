t = int(input())
import math
for i in range(t):
    n = int(input())
    x = float(input())
    ans = n * math.floor(x)
    kasr = 1/n
    ans += n - math.ceil(n * (1 - (x - math.floor(x))))

    print(ans)
