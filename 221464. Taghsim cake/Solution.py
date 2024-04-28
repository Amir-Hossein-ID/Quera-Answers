t = int(input())
import math

def gcd(a,b):
    while b:
        a,b = b, a%b
    return a

for i in range(t):
    n, k = map(int, input().split())
    s = gcd(n,k)
    n //= s
    k //= s
    kk = math.log2(k)
    if kk != int(kk):
        print(-1)
        continue
    print(int(kk))
