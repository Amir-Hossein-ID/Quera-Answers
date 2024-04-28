n = int(input())
m = [int(i) for i in input().split() if int(i) > 1]
print(min(len(m)+2, n))
