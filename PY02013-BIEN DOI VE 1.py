def sol(x) :
    ans = 1
    while(x!=1) :
        if (x % 2 == 0) :
            x //= 2
        else : x = x * 3 + 1
        ans += 1
    print(ans)
while (True) :
    x = int(input())
    if (x == 0) : break
    sol(x)
