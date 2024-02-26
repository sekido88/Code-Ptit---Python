n = int(input())
i = 0
v = []
d = [0] * 202
while (i != n) :
    a = [int(i) for i in input().split()]
    for value in a :
        d[value] = 1
        v.append(value)
    i += len(a)
mx = max(v)
res = 0
for i in range(1,mx + 1,1) :
    if (d[i] == 0) : 
        res = 1
        print(i)
if res == 0 : print("Excellent!")
