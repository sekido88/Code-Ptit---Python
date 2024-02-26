#by sekido
def rev( x ) :
    s = 0
    while (x > 0) :
        s = s * 10 + (int)(x%10)
        x //= 10
    return s
def res( x ) :
    if ( x%7 == 0 ) :
        print(x)
        return
    check = 1
    v = rev(x)
    v2 = x
    N = v + v2
    while (N % 7 != 0 and check <= 1000) :
        check += 1
        N = v + v2 
        v = N
        v2 = rev(N)
    if (check > 1000) :
        print(-1)
        return
    print(N)

t = int(input())
for _ in range(t) :
    x = int(input())
    res(x)
