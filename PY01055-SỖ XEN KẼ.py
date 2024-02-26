# by sekido
def check(x) :
    if (len(x) % 2 == 0) : return False
    if (len(x) == 1) : return True
    if (x[0] == x[1]) : return False
    for i in range(2,len(x),2) :
        if (x[i] != x[i-2]) : return False
    return True

def solve(v) :
   if (check(v)) : print("YES")
   else : print("NO")
    
t = int(input())
for _ in range(t) :
    v = str(input())
    solve(v)