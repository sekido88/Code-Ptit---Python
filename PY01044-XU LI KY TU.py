x = input().split()
y = input().split()

dd = {}
res1 = []
res2 = []
for i in x :
    
    i = i.lower()
    dd[i] = 1

dd2 = {}
for j in y :

    j = j.lower()
    if (j not in dd) :
        dd[j] = 1
    else :
        dd2[j] = 1

dd = dict(sorted(dd.items()))
dd2 = dict(sorted(dd2.items()))
for i in dd.keys() :
    print(i,end = " ")
print()
for j in dd2.keys() :
    print(j,end = " ")
