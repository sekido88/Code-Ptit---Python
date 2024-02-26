n , m = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
dd = [0] * 501
for i in a :
    dd[i] += 1
mx = max(dd)
mx2 = 0
res = 0
for i in range(0,m + 1,1) :
    if (dd[i] != 0) :
        if ( mx2 < dd[i] and dd[i] < mx ) :
            mx2 = dd[i]
            res = i
if (res == 0) : 
    print("NONE")
else :
    print(res)