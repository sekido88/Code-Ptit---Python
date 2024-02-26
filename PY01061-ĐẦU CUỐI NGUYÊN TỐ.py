# by sekido
def C_Pr(x) :
    if(x<2) : return False
    i = 2
    while(i*i<=x) :
        if(x%i==0) : return False
        i = i + 1
    return True
def check(x) :
    numd = 0
    numc = 0
    for i in range(0,3) :
        numd = numd * 10 + int(x[i])
    for j in range(len(x)-3,len(x)) :
        numc = numc * 10 + int(x[j])
    
    if (C_Pr(numd) and C_Pr(numc)) : return "YES"
    else : return "NO"

def solve(v) :
   print(check(v))
    
t = int(input())
for _ in range(t) :
    v = str(input())
    solve(v)