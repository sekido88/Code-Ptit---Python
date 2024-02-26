def solve(x ):
    s = 0
    if (x % 2 == 0) :
        for i in range(2,x+1,2) :
            s = s + float(1/i)
    else :
        for i in range(1,x+1,2) :
             s = s + float(1/i)
    print(f"{s:.6f}")
t = int(input())
for _ in range(t) :
    v = int(input())
    solve(v)