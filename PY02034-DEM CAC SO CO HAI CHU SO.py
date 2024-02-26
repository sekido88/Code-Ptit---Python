s = str(input())
dd = [0] *1002
a = []
ok = 0
if (len(s) % 2 != 0) : ok = 1
vip = 0
for i in range(0,len(s) - ok,2) :
    vip = (vip + int(s[i])) * 10 + int(s[i+1])
    dd[vip] += 1
    a.append(vip)
    vip = 0
for i in a :
    if(dd[i] != 0) :
        print(i,dd[i])
        dd[i] = 0


