n =int(input())
a = {'R':0, 'U':1, 'L':2, 'D':3}

now = 'R'

s = input()
ans = ''
for i in s:
    if i != now:
        aa = a[i] - a[now]
        ans += 'R' * (aa if aa > 0 else 4+aa)
        now = i
    ans += 'F'
print(ans)
