# by sekido
def check(x) :
    s = 0
    for i in x :
        s += int(i)
    snew = s
    srev = 0
    while(s > 0) :
        srev = srev * 10 + int(s%10)
        s = s//10
    return(snew >=10 and snew == srev)

def solve(v) :
   if check(v) : print("YES")
   else : print("NO")
    
t = int(input())
for _ in range(t) :
    v = str(input())
    solve(v)