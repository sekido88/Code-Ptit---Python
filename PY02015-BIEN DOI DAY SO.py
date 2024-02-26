#by sekido 

def check( a) :
    if (a.count(0) == 4) : return True
    return False

while( True ):
    ans  = 0
    a = [int(i) for i in input().split()]
    if( check(a) ) : break
    while ( a.count(a[0]) != 4 ) :
        tmp = 0     
        for j in range(4) :
            if (j == 0) :
                tmp = a[0]
            if (j == 3) : 
                a[3] = abs(a[3]-tmp)
            if (j < 3 ) : 
                a[j] = abs(a[j] - a[j+1]) 
        ans += 1    
    print(ans)