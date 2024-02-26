m , n = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
dic = {v : 1 for v in a} 
dic2 = {v : 2 for v in b}
def out(a) :
    for i in a :
        print(i,end = " ")
    print()
x , y , z = [] , [] , []
for i in dic.keys() :
    if ((i in dic2.keys())) :
        x.append(i)
for i in dic.keys() :
    if (not(i in dic2.keys())) :
        y.append(i)
for i in dic2.keys() :
    if (not(i in dic.keys())) :
        z.append(i)
x.sort()
y.sort()
z.sort()
out(x)
out(y)
out(z)