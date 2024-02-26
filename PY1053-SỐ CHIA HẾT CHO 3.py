# by sekido
def C_Pr(x) :
    if(x<2) : return False
    i = 2
    while(i*i<=x) :
        if(x%i==0) : return False
        i = i + 1
    return True
def check(x) :
    s = 1
    for i in x :
        if (i != '0') : s = s * int(i)
    return s

def solve(v) :
   print(check(v))
    
t = int(input())
for _ in range(t) :
    v = str(input())
    solve(v)