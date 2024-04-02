from sys import setrecursionlimit as setlimit
setlimit(3000)
n  = int(input())
ans = 0
def do(l):
    if len(l)>2:
        mi = min(l[0],l[-1])
        if max(l[1:-1]) <= mi:
            for i in l[1:-1]:
                if mi-i>0:
                    global ans
                    ans += mi-i
            return
        else:
            c = l[1:-1].index(max(l[1:-1]))
            do(l[:c+2])
            do(l[c+1:][::-1])
    
do([int(i) for i in input().split()])
print(ans)
