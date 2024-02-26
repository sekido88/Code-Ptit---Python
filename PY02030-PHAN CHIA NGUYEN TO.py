def nt(x) :
    i = 2
    while (i * i <= x) :
        if (x % i== 0) :
            return False
        i += 1
    return (x >= 2)
n = int(input())
a = [int(i) for i in input().split()]
dd = { x : 1 for x in a}
a = list(dd.keys())
s = sum(a)
si = 0
ok = 0
for i in range(0,len(a)) :
    si += a[i]
    if (nt(si) and (nt(s-si))) :
        print(i)
        ok = 1
        break
if (ok == 0) :
    print("NOT FOUND")
