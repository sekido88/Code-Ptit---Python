for _ in range(int(input())) :
    n = int(input())
    a = [int(i) for i in input().split()]
    d = {}
    d = {x : 1 for x in a}
    mx = max(a)
    mn = min(a)
    res = 0
    for j in range(mn,mx + 1,1) :
        if j not in d :
            res += 1
    print(res)