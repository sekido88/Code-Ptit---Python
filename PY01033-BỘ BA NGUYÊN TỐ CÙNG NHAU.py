def gcd( a , b) :
    if (b == 0) : return a
    return gcd( b , a % b)
n = [int(i) for i in input().split()]
l , r = n[0] , n[1]
for i in range(l,r+1) :
    for j in range(i+1,r+1) :
        t = gcd( i , j)
        if( t == 1) :
            for k in range(j+1,r+1) :
                if(gcd(i,k) == 1 and gcd(j,k) == 1) :
                    print("("+str(i)+", "+str(j)+", "+str(k)+")")


