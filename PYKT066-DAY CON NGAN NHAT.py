import math
def gcd(a , b) :
   return math.gcd(a,b)
t = int(input())
for _ in range(t) :
    n , k = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    res , tmp , ok = 1001 , 1 , 0
    for i in range(n) :
        tmp = a[i]
        if (a[i] == k) :
            res = 1
            ok = 1
            break
        for j in range(i + 1, n) :
            tmp = gcd(tmp , a[j])
            if (tmp == k) :
                res = min (res , j - i + 1)
                ok = 1
    if (ok == 0 ) : print("-1")
    else : print(res)
    