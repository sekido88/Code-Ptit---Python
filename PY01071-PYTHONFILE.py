# by sekido
def check(x) :
    if (len(x) < 3) : return "no"
    r = ""
    for i in range(3,0,-1) :
        r = r + x[len(x) - i]  
    r = r.lower()
    if (r == ".py") : return "yes"
    return "no"
def solve(v) :
   print(check(v))
    
t = 1
for _ in range(t) :
    v = str(input())
    solve(v)