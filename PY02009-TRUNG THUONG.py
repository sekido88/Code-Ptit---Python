def max(a,b) :
    if (a > b) : return a
    return b
def res(v ) :
    dd = [0] * 1002
    max_1 = 0
    ans = 1001
    for i in v :
        dd[i] += 1
        max_1 = max(max_1 , dd[i])
    for i in v:
        if (dd[i] == max_1) :
            if (i < ans) :
                ans = i
    print(ans)

t = int(input())
for _ in range(t) :
    a = []
    n = int(input())
    for i in range(n) :
        v=int(input()) 
        a.append(v)
    res(a)
       