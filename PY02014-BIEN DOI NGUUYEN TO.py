#by sekido 
def nt(x) :
    i = 2
    while(i * i <= x) :
        if (x % i == 0) :
            return False
        i += 1
    return (x >= 2)
def B1(a,x) :
    res = -1
    l , r = 0 ,len(a) - 1
    while ( l <= r ) :
        m = (l + r)//2
        if (a[m] >= x ) : 
            res = a[m]
            r = m - 1
        else :
            l = m + 1
    return res
def B2(a,x) :
    res = -1
    l , r = 0 ,len(a) - 1
    while ( l <= r ) :
        m = (l + r)//2
        if (a[m] <= x ) : 
            res = a[m]
            l = m + 1
        else :
            r = m - 1
    return res
a = []
for i in range(10005) :
    if (nt(i)) :  a.append(i)
# for i in range(50) :
#     print(a[i],end = " ")
#     if (i%10 == 0) : print()
ans = 0
t = int(input())
x = [int(i) for i in input().split()]
for j in x :
    ans = max (ans ,min(abs(j - B1(a,j)),abs(j - B2(a,j))) )
print(ans)