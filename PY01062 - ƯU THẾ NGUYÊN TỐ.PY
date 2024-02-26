# by sekido
def pr (x) :
    if (x<2) : return False
    i = 2
    while (i * i <= x) :
        if (x % i == 0) :
            return False
        i += 1
    return True
def check(x) :
    count_pr = 0
    count_notpr = 0
    if (not (pr(len(x))) ): return False
    for i in range(0,len(x)) :
        if ( pr( int( x[i]))) :
            count_pr += 1
        else : count_notpr += 1
    return (count_notpr < count_pr)
def solve(v) :
   if (check(v)) : print("YES")
   else : print("NO")
    
t = int(input())
for _ in range(t) :
    v = str(input())
    solve(v)