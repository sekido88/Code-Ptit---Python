def anl ( x ) :
    print(1,end=" * ")
    for i in range(2,x+1) :
        count = 0
        if (x % i == 0) :
            while (x % i == 0 and x > 0) :
                count += 1
                x = x / i
            print(str(i) + '^' + str(count),end = "")
            if(x != 1) : print(' * ',end = "")
            count = 0
    print()
        
t = int(input())
for _ in range(t) :
    x = int(input())
    anl(x)
