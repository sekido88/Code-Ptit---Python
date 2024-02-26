def Make_Round(x) :
    v = 0
    remember = 0
    a = []
    check = 0
    if (x<5) :
        print(0)
        return
    while(x > 0) :
        v = int( x%10 )
        x = x/10
        if ( v >= 5 and x>= 9) :
            v = 0
            x += 1
        if (v<5 and x>=9) :
            v = 0
        a.append(v)
        if (x<=9 and check == 1) : break
        if (x<=9) : check = 1
        
    a.reverse()
    if (a[1] < 5) : a[1] = 0
    if (a[1] >=5) :
        a[1] = 0 
        a[0] += 1
    for i in a :
        print(i,end="")
    print()
t = int(input())
while (t>0) :
    t -= 1
    x = int(input())
    if(x <= 9) : print(x)
    else : Make_Round(x)