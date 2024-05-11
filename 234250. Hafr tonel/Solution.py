t = int(input())

for i in range(t):
    m = int(input())
    k = [[int(i) for i in input().split()] for j in range(m)]
    chosen_x = k[0][0]
    chosen_y = k[0][1]
    s = []
    for j in k:
        if j[0] != chosen_x:
            s.append(j[1])
    if all([p == s[0] for p in s]):
        print('YES')
        continue
    s = []
    for j in k:
        if j[1] != chosen_y:
            s.append(j[0])
    if all([p == s[0] for p in s]):
        print('YES')
        continue
    print('NO')
