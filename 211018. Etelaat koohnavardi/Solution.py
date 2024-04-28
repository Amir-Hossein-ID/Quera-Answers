a = int(input())

b = input().split()
c = b.count('1')
d = b.count('2') % 2
if d and c > 1:
    print((c-2)%2)
elif d:
    print(d*2-c)
else:
    print(c%2)
