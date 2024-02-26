def res(s) :
    s = " " + s
    check = 1
    ans = ""
    for i in range(len(s)-1,0,-1) :
        if (check == 3) :
            ans = ',' + s[i] + ans
            check = 1
        else : 
             check += 1
             ans = s[i] + ans
    if(ans [0] == ',') :
        for i in range(1,len(ans)) :
            print(ans[i],end="")
    else :
     print(ans)

t = 1
for _ in range(t) :
    x = (input())
    res(x)
    
    
