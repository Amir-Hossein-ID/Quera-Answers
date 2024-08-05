import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = print
print = sys.stdout.write

t = int(input())
a = list(maput())

M = 1000000007

if t == 0 or a[0] % 2:
    print('0')
    exit(0)

ans = 1

mi = a[0] // 2
ma = a[0] // 2
options = 0

for i in a[1:]:
    if i == mi + ma:
        ans *= ma - mi + 1
        ans %= M
    elif i > mi + ma:
        ma = i - mi
        if ma < mi:
            print('0')
            exit(0)
    else:
        mi = i - ma
        if mi > ma:
            print('0')
            exit(0)

print(str(ans))
