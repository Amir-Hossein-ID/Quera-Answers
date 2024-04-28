t = int(input())

for i in range(t):
    n = int(input())
    s = input()
    a=s.count('Q')
    b=s.count('C')
    if a > b:
        print("Quera")
    else:
        print("CodeCup")
