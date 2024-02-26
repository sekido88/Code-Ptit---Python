# by sekido
def check(x) :
    xrv = x[::-1]
    for i in range(1,len(x)) :
        if (abs(ord(x[i])-ord(x[i-1])) != abs(ord(xrv[i]) - ord(xrv[i-1])) ) : return "NO"
    return "YES"

def solve(v) :
   print(check(v))
    
t = int(input())
for _ in range(t) :
    v = str(input())
    # print(v[::-1])
    solve(v)