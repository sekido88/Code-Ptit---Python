def res(a) :

    if ( len(a) < 4 ) : return "NO"
    for i in a :
        if (i.isdigit()) :
            if (int(i) > 255 or int(i) < 0) : 
               return "NO"
        else : return "NO"
    return "YES"
    
t = int(input())
for _ in range(t) :

    x = input().split('.')
    print(res(x))
