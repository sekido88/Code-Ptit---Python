def gcd( a , b) :
    if (b == 0) : return a
    return gcd( b , a % b)
def mu (x , y) :
    res = 1
    while (y > 0) :
        if (y % 2 == 1) : res = res * x
        x *= x
        y//=2
    return res
n = [int(i) for i in input().split()]
N , K = n[0] , n[1]
check = 0
for i in range(mu(10,K - 1),mu(10,K)) :
    if (gcd(i , N) == 1) :
        print(i,end=" ")
        check += 1
    if (check == 10) : 
        print()
        check = 0

