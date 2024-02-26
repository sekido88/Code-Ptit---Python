def haha (a , mx , mn) :
    for i in a :
        if (i != mx and i != mn) :
            return False
    return True
while( True ) :
    x = int(input())
    if (x == 0) : break
    a = []
    for _ in range(x) : 
        a.append(int(input())) 
    mx = max(a)
    mn = min(a)
    if (haha(a, mx , mn)) : 
        print("BANG NHAU")
    else : print(mn , mx)
