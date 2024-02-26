#by sekido
def gcd( a , b) :
    if (b == 0) : return a
    return gcd( b , a % b)
n = int(input())
a = [int(i) for i in input().split()]
a . sort()
for i in range(len(a) ) :
    for j in range(i+1 , len(a) ):
        t = gcd( a[i] , a[j])
        if( t == 1) :
           print(a[i] , a[j])


