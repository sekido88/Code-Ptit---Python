# a = [0,1,2,3,4,5,6,7,8,9,10]
def check(v) :
    d = {}
    for i in range(0,2) :
       d [v[i]] = 1
    for i in range(2,len(v)) :
        if (v[i] != v[i-2]) : return False
        d [v[i]] = 1
    return (len(d) == 2)
def solve(v) :
   if check(v) : print("YES")
   else : print("NO")
    
t = int(input())
for _ in range(t) :
    v = (input())
    solve(v)