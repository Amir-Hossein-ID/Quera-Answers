import sys

input = lambda: sys.stdin.readline().strip()
maput = lambda: map(int, input().split())
printf = print
print = sys.stdout.write

r = int(input())
c = int(input())

a = {1:[3,4,2], 2:[1,3,4,6,5], 3:[1,2,4,6,7], 4:[1,2,3,5,6,7], 5:[2,4,6], 6:[2,5,4,3,7], 7:[3,4,6]}

if c in a[r]:
    print('1')
else:
    print('2')
