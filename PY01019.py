def check ( s1 ) :

    s2 =  ""
    for i in range(len(s1)-1,-1,-1) :
        s2 = s2 + s1[i]
        # print(s1[i])
    for i in range(1,len(s1)-1) :
        if (abs(ord(s1[i]) - ord(s1[i-1])) != abs(ord(s2[i]) - ord(s2[i-1]))) :
           return False
    return True
t = int(input())
for _ in range(t) :
    x = input()
    if(check(x)) : print("YES")
    else : print("NO")
