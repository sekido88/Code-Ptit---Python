def check_Pr(x) :
    if(x<2) : return False
    i = 2
    while(i*i<=x) :
        if(x%i==0) : return False
        i = i + 1
    return True
def check_Re_To_Co(x) :
    v = 0
    s = 0
    while(x>0) :
        v = v*10 + int(x%10)
        if (not check_Pr(int(x%10))) : return False
        s = s + int(x%10)
        x//=10
    return (check_Pr(v) and check_Pr(s))
# main () 
test_case = int(input())
while(test_case>0) :
    v = int(input())
    if(check_Pr(v) and check_Re_To_Co(v)) : print("Yes")
    else :print("No")
    test_case -= 1