#sekido
def gcd (a, b) :
    if (a == 0) :return b 
    return gcd(b%a, a)
t = int(input())
for _ in range(t) :
    a = int(input())
    b = int(input())
    print(gcd(a,b))