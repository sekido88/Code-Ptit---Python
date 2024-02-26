# a = [0,1,2,3,4,5,6,7,8,9,10]
def check_Pr(x) :
    if(x<2) : return False
    i = 2
    while(i*i<=x) :
        if(x%i==0) : return False
        i = i + 1
    return True
def check(x) :
    num = 0
    b = 4
    if (len(x) == 3) : b = 3
    for i in range(len(x)-b,len(x)) :
        num = num * 10 +int(x[i])
    return (check_Pr(num))
def solve(v) :
   if check(v) : print("YES")
   else : print("NO")
    
t = int(input())
for _ in range(t) :
    v = str(input())
    solve(v)