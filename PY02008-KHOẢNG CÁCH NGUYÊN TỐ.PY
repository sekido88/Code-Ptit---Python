# by sekido
def check(x) :
    if(x<2) : return False
    i = 2
    while(i*i<=x) :
        if(x%i==0) : return False
        i = i + 1
    return True
def solve(u , v) :
    d = {}
    count = 0
    m_prime = 0
    for i in range(10000) :
        if (check(i)) : 
           d[i] = 1
           count += 1
           m_prime = i
        if (count == u) : break
    count = v

    for i in d :
        print(count,end = " ")
        count = count + i
    print(count)

    # i = v
    # while (i <= 10000) :
    #     ok = 0
    #     for j in range(i+1,10000) :
    #         if (not ((j-i) in d ) ) : continue
    #         else : 
    #             if (d[j-i] == 0) : continue
    #             count += 1
    #             print(i,end= " ")
    #             if (count == u) : print(j)
    #             d[j-i] = 0
    #             i = j
    #             break
    #     # print(i)
    #     if (count == u) : break
    
t = 1
for _ in range(t) :
    a = [int(i) for i in input().split()]
    u = a[0]
    v = a[1]
    solve(u,v)