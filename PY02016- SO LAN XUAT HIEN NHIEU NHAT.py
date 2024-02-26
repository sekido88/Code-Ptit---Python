
def res(a ) :
    ans = 10**6 + 1
    dd = [0] * ((10**6) + 1)
    count = 0
    for i in a :
        dd[i] += 1
        count = max(count,dd[i])
    for value in a :
        if (dd[value] == count) :
            if (value < ans) :
                ans = value
    if (dd[ans] < len(a)/2) : 
        print("NO")
        return
    print(ans)
     
t = int(input())
for _ in range(t) :
    n = int(input()) 
    x = [int(i) for i in input().split()]
    res(x)
