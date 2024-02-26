# by sekido
def C_Pr(x) :
    if(x<2) : return False
    i = 2
    while(i*i<=x) :
        if(x%i==0) : return False
        i = i + 1
    return True
def check(x) :
    s = 0
    for i in range(0,len(x)) :
        s = s + int(x[i])
        if ( C_Pr(i) and not( C_Pr( int(x[i]) ) )) : return False
        elif ( not(C_Pr(i)) and C_Pr(int(x[i]) ) ) : return False
    return True

def solve(v) :
   if (check(v)) : print("YES")
   else : print("NO")
    
t = int(input())
for _ in range(t) :
    v = str(input())
    solve(v)