# by sekido
def check(x) :
    s = 0
    t = 1
    count_chan = 0
    count_0 = 0
    for i in range(0,len(x)) :
        if ( i & 1) :
            if (x[i] != '0') : t *= int(x[i])
            else : count_0+=1
        else :
            count_chan += 1
            s += int(x[i])
    if (count_chan + count_0 == len(x)) : t = 0
    print(s,t)
def solve(v) :
#    if (check(v)) : print("YES")
#    else : print("NO")
    check(v)
    
t = int(input())
for _ in range(t) :
    v = str(input())
    solve(v)