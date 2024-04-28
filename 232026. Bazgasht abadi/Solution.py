t = int(input())

def x(a):
    if a%4==2:
        return 1
    elif a%4==0:
        return 2
    else:
        return x(a-1) - 4
for i in range(t):
    n = int(input())
    if n==1:
        print(2)
    else:
        print(x(n))
