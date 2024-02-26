def check_Pr(x) :
    if(x<2) : return False
    i = 2
    while(i*i<=x) :
        if(x%i==0) : return False
        i = i + 1
    return True
def Va_R(x) :
    v_r = 0
    while(x>0) :
        v_r = v_r*10 + int(x%10)
        x//=10
    return v_r
def check_Re(x) :
    if (x < 9) : return False
    v_r = 0
    n = x
    while(x>0) :
        v_r = v_r*10 + int(x%10)
        x//=10
    return (check_Pr(v_r) and n!=v_r)
# main () 
dp = []
# for i in range(1,1000001) :
#     dp.append(0)
# for i in range(1,1000001) :
#     if(check_Pr(i) and check_Re(i)) :
#         dp[i] = 1
test_case = int(input())
while(test_case>0) :
    v = int(input())
    for i in range(1,v) :
        if (check_Pr(i) and check_Re(i)) :
            v2 = Va_R(i)
            if (v2 < v and i<v2) : print(i,v2,end=" ")
    print()
    test_case -= 1