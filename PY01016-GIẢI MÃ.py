def res( x ) :
    for i in range(0,len(x),2) :
        for j in range(0,int(x[i+1])) :
            print(x[i],end="")
    print()
t = int(input())
while (t > 0) :
    x = str(input())
    res(x)
    t-=1