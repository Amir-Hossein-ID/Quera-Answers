import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = print
print = sys.stdout.write

t = int(input())

for i in range(t): # seems like a bad solution, but anyway
    n = int(input())
    a = maput()
    c = [0,0,0,0]
    for i in a:
        c[i-1] += 1
    c[2], c[0] = max(c[2] - c[0], 0), max(c[0] - c[2], 0)
    c[0] %= 4
    c[1] %= 2
    ans = 0
    mini = 0
    if c[2]:
        ans = c[2]
        mini = 1
        if c[1]:
            mini = 2
            ans += 2 * c[1]
    else:
        aa = 2*c[1] + c[0]
        aa %= 4
        if aa:
            ans += 4 - aa
            mini = 4 - aa
    ans -= mini
    print(str(max(ans, 0)) + '\n')
