q, t = map(int, input().split())
last = 0
c = 0
for i in range(q):
    s = int(input())
    if (s-1) % (t+1) == 0:
        print('Peygir')
        continue
    s -= (s-1) // (t+1) + 1
    last =s % 3
    if last==1:
        print('Tannaz')
    elif last == 0:
        print('Morshed')
    elif last == 2:
        print('Jeddy')
