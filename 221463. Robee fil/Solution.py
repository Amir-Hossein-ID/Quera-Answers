n,m = map(int, input().split())

print('A'*m)
for i in range(n-2):
    print('A', end='')
    if (m>1):
        print('.'* (m-2), end='')
        print('B', end='')
    print()
if (n>1):
    print('A', end='')
    print('B'*(m-1))
