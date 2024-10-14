import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = print
print = sys.stdout.write

from collections import Counter

t = int(input())
for i in range(t):
    n = int(input())
    a = Counter()
    for i in range(n):
        b = Counter(input())
        for i in b:
            a[i] = max(a[i], b[i])
    ans = sum(a.values())
    print(str(ans) + '\n')
