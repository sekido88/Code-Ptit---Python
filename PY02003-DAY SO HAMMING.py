N = 10 ** 18
lis = [0]
i = 1
while (i <= N ) :
    j = 1
    while ( j <= N ) :
        k = 1
        while ( k <= N ) :
            lis += [i*j*k]
            k *= 5
        j *= 3
    i *= 2
lis.sort()
def res(a , x) :
    l , r = 0 , len(a) - 1
    while(l <= r) :
        m = (l + r) // 2
        if (a[m] == x) : return m
        elif  (a[m] < x) : l = m + 1
        else : r = m - 1
    return "Not in sequence"
for _ in range(int(input())) :
    x = int(input())
    print(res(lis,x)) 
    