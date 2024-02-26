d = [0] * 1000002
t = int(input())
for _ in range(t) :
    n = int(input())
    a = [int(i) for i in input().split()]
    res = 0
    for i in a :
        d[i] += 1
    for i in a :
        if (d[i] % 2 != 0) :
            res = i
        d[i] = 0
    print(res)
    

