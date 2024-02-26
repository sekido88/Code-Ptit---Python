def check ( s1 ) :
    if( len(s1) <= 1 ) : return False
    b = int(s1[len(s1)-2]) * 10 + int(s1[len(s1)-1])
    if (b == 86) : return True
    return False
t = int(input())
for _ in range(t) :
    x = input()
    if(check(x)) : print("YES")
    else : print("NO")
