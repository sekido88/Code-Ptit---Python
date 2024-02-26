#by sekido
def check (x ) :
    s , s1 = 0 , x 
    while(x > 0) :
        s += (x%10)
        x //= 10
    return (s,s1)
def res (a) :
    a.sort(key = check )    
    for value in a :
        print(value,end = " ")
t = int(input())
for _ in range(t) :
    n = int(input())
    a = [int(i) for i in input().split()]
    res(a)
    print()