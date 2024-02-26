#by sekido
n , m = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
def check (a, b) :
    if (len(a) != len(b)) : return False
    v = []
    for i in a.keys() :
        v.append(i)
    pos = 0
    for j in b.keys() :
        if (v[pos] != j) :
            return False
        pos += 1
    return True
dd = {}
dd2 = {}
for i in a :
    dd[i] = 1
for i in b :
    dd2[i] = 1
# for i in dd.keys() :
#     print(i , end = " ")
# print()
# for j in dd2.keys() :
#     print(j,end = " ")
if check(dd,dd2) :
    print ("YES") 
else :
    print("NO")