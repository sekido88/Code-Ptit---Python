def gcd( a , b) :
    if (b == 0) : return a
    return gcd( b , a % b)
def res( x ):
    v1 = x
    v2 = 0
    while (x > 0) :
        v2 = v2*10 + int(x%10)
        x//=10
    if(gcd(v1,v2) == 1) : print("YES")
    else : print("NO")
t = int(input())
for _ in range(t) :
    x = int(input())
    res(x)