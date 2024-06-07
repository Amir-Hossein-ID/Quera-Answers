n = int(input())

t1 = [2,0,1,6,4,5]
t2 = [2,1,3,7,8,9]

if n >= 33:
    print(-1)
else:
    print(*t1, sep = ' ')
    print(*t2, sep = ' ')
