def check ( a , b) :
    a.sort()
    b.sort()
    for i in range(len(a)) :
        if (a[i] > b[i]) : return "NO"
    return "YES"
t = int(input())
for _ in range(t) :
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(j) for j in input().split()]
    print( check( a, b))