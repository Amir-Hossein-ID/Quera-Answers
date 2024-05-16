h,k = int(input()), int(input())

if h%2==0:
    if k%2==0:
        print('YES')
    else:
        print('NO')
else:
    if k>=2 and k%2==0:
        print('YES')
    else:
        print("NO")
