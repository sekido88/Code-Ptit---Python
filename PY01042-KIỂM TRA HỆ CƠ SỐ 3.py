# a = [0,1,2,3,4,5,6,7,8,9,10]
def check(x) :
    d = {}
    d ['0'] , d['1'] , d['2'] = 1,1,1
    for i in range(len(x)) :
        d[x[i]] = 1
    return (len(d) == 3)
def solve(v) :
   if check(v) : print("YES")
   else : print("NO")
    
t = int(input())
for _ in range(t) :
    v = str(input())
    solve(v)