#by sekido
nt = [1] * (10**6 + 1)
def dp_pr() :
    nt [0] ,nt[1] = 0 , 0
    i = 2
    while( i*i <= 10**6) :
        if (nt[i] == 1) :
            for j in range(i*i,10**6+1,i) :
                nt[j] = 0
        i += 1
def res( n ) :
    ans = 0
    for i in range(n-6) :
        if ( (nt[i] and nt[i+6]) and (nt[i+2] or nt[i+4]) ) :
            # print(i,i+2,i+6)
            ans += 1
    print(ans)
dp_pr()
t = int(input())
for _ in range(t) :
    x = int(input())
    res(x)