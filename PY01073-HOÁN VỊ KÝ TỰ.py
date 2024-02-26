
def out( s ) :
    print(s)

dd = []
s = input()
def res (j , n , v) :

    for i in range(0,n + 1 ) :
        if (dd[i] == 0) :
            dd[i] = 1
            if (j == n) :
                out(v + s[i])
            else :
                res(j+1, n, v + s[i])
            dd[i] = 0
           
for i in range(len(s)+1) :
    dd.append(0)
res(0,len(s) - 1,"")

