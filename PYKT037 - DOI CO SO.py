# Sekido
tmp = ""
for i in range(0,10) :
    tmp += str(i)
i = ord('A')
while (i <= ord('Z')) :
    tmp += chr(i)
    i += 1
def res(n, b) :
    ans = ""
    while ( n > 0) :
        du = int( n % b )
        ans = tmp[ du ] + ans
        n //= b
    print(ans) 
for _ in range(int(input())) :

    n , b = [int(i) for i in input().split()]
    res(n,b)