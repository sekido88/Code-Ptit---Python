def check(s) :
    total = int(s[0]) 
    for i in range(1,len(s)) :
        total = total + int(s[i])
        if (abs(int( s[i]) - int( s[i-1])) != 2) :
            return False
    return (total % 10 == 0)
    
t = int(input())
for _ in range(t) :
    x = (input())
    if(check(x)) :
        print("YES")
    else : print ("NO")
    
