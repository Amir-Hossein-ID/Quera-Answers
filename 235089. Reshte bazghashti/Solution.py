n =int(input())
a = {0 :"sefr",
1 :	"yek",
2 :	"do",
3 :	"se",
4 :	"chahaar",
5 :	"panj",
6 :	"shesh",
7 :	"haft",
8 :	"hasht",
9 :	"noh",
10:"dah",
11:"yaazdah",
12:"davaazdah",
13:"sizdah",
14:"chahaardah",
15:"paanzdah",
16:"shaanzdah",
17:"hifdah",
18:"hijdah",
19:"noozdah"}
d = {
    10:'dah',
20:"bist",
30:"si",
40:"chehel",
50:"panjaah",
60:"shast",
70:"haftaad",
80:"hashtaad",
90:"navad",
}

s = {
100:"sad",
200:"devist",
300:"sisad",
400:"chahaarsad",
500:"paansad",
600:"sheshsad",
700:"haftsad",
800:"hashtsad",
900:"nohsad",
}

def make(n):
    if n < 20:
        return a[n]
    elif n < 100:
        return d[n//10*10] + ('o' + a[n%10] if n%10 else '')
    else:
        # print(n)
        # print(n//100*100, (n%100)//10*10, n%10)
        pp = (n%100)//10*10
        if pp == 10:
            return s[n//100*100] + 'o' + a[n%100]
        return s[n//100*100] + ('o' + d[(n%100)//10*10] if (n%100)//10*10 else '') + ('o' + a[n%10] if n%10 else '')

last = 'sefr'
for i in range(1, n+1):
    last = last + make(len(last)%1000)

print(last)
