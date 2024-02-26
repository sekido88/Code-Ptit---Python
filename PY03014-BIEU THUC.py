t = int(input())
for _ in range(t) :
    x = input()
    a = []
    cnt_1 = 0
    cnt_2 = 0
    i = 0
    dd = {}
    while(i < len(x) ) :
        if ( x[i] == '(' ) :
            while ( x[i] == '(') :
                cnt_1 += 1
                dd[cnt_1] = 1
                print(cnt_1,end = " ")
                i += 1
            i -= 1        

        if (x[i] == ')') :
            cnt_2 = cnt_1
            while(i < len(x) and x[i] == ')') :
                if (dd[cnt_2] == 1 ) : print(cnt_2,end = " ")
                dd[cnt_2] = 0
                cnt_2 -= 1
                i += 1
            i -= 1
        i += 1
    for j in dd.keys() :
        if (dd[j] == 1) :
            print(j,end = " ")
    print()
    


            
