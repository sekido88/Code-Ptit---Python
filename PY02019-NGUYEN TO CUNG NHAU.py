#by sekido
def gcd( a, b) :
    if ( b == 0 ) : return a
    return gcd ( b, a%b )
def res(a ) :
    a.sort()
    for i in range(0, len(a)) :
        for j in range(i+1, len(a)) :
            if (gcd (a[i],a[j]) == 1) :
                print(a[i],a[j])
# print(gcd(5,10))
t = int(input())
a = [int(i) for i in input().split()]
res(a)
