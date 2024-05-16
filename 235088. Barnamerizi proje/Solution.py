n =int(input())
l,r = [int(i) for i in input().split()]

opt = r - l

ans = n//r
opt *= ans
if n%r==0:
    print(ans)
elif n%r > l:
    print(ans+1)
else:
    if n%r + opt > l:
        print(ans+1)
    else:
        print(-1)
