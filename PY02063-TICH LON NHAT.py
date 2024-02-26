def rev ( v ) :
    return -v
n = int(input())
a = [int(i) for i in input().split()]
a.sort(key = rev)
res = - 1000 * 1000 * 10000
mx = max(a)
mn = min(a)
d = 0
dd = {}
# a.append(pow(10,-10))
# a.append(pow(10,-10))
for i in range(n) :
    if (i + 2 < n ) :
        res  =  max(res, max( a[i]*a[i+1]*a[i+2],a[i+1] * a[i + 2]) )
    if (i + 1 < n) :
        res =   max(res,a[i] * a[i + 1])
    if (i != 0) :
        res = max(res,mx*a[i])
    if (mn == a[i] ) :
        if (d == 0) : 
            d = 1
            continue
        res = max(res , mn * a[i])
res = max(res , a[0] * a[n - 1] * a[n - 2])
print(res)