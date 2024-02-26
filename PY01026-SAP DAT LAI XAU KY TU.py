def res (a , b) :
    d = {}
    for i in a :
        if (i not in d) :
            d[i] = 1
        else : d[i] += 1
    for j in b :
        if (j not in d) :
            return "NO"
        else : 
            d[j] -= 1
            if (d[j] < 0) : return "NO"
    return "YES"


for _ in range( 1,int(input()) + 1 ) :
    a = input()
    b = input()
    print("Test "+str(_)+":",res(a,b))
