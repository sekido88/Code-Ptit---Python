# def check(x) :
#     if(x<2) : return False
#     i = 2
#     while(i*i<=x) :
#         if(x%i==0) : return False
#         i = i + 1
#     return True
# def gcd(a,b) :
#     if (b == 0) : return a
#     return gcd(b,a%b)
# def mu(x , y) :
#     res = 1
#     while(y>0) :
#         if(y%2==0) : res *= x
#         x*=x
#         y/=2
#     return res
def res (sochuso,v) :
    res = 0
    for i in range (2,9,2) :
        res = i
        if (sochuso==2) :
            res = res * 10 + i
            if (res < v) : print(res, end=" ")
            res = i
        for j in range (0,9,2) :
            res = res * 10 + j
            if (sochuso==3) :
                res = res * 10 + i
                if (res < v) : print(res,end=" ")
                res = i
            if (sochuso==4) :
                res = res * 10 + j
                res = res * 10 + i
                if (res < v) : print(res,end=" ")
                res = i
            for k in range (0,9,2) :
                res = res * 10 + k
                if (sochuso == 5):
                    res = res * 10 + j
                    res = res * 10 + i
                    if (res < v): print(res,end=" ")
                    res = (res//1000)
                if (sochuso == 6):
                    res = res * 10 + k
                    res = res * 10 + j
                    res = res * 10 + i
                    if (res < v) : print(res,end=" ")
                    res = (res//10000)
            res = i
def Ham(x) :
    s = 0
    while(x > 0) :
        s += 1
        x //= 10
    return s

t = int(input())
# res(2,100)
while (t>0) :
    n = int(input())
    n2 = n
    for i in range(0,Ham(n2)+1,2) :
        res(i, n)
    print()
    t-=1


1