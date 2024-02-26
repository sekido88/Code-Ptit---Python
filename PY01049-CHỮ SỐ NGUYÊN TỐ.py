# a = [0,1,2,3,4,5,6,7,8,9,10]
def C_Pr(x) :
    if(x<2) : return False
    i = 2
    while(i*i<=x) :
        if(x%i==0) : return False
        i = i + 1
    return True
def check(x) :
    if( not(C_Pr(len(x))) ) : return False
    u , v = 0 , 0
    for value in x :
        if (C_Pr(int(value))) : u+=1
        else : v+=1
    return (u > v)

def solve(v) :
   if check(v) : print("YES")
   else : print("NO")
    
t = int(input())
for _ in range(t) :
    v = str(input())
    solve(v)