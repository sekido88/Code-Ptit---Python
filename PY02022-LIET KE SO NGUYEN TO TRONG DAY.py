#by sekido
def nt( x) :
    i = 2
    while(i * i <= x) :
        if (x % i == 0) :
            return False
        i += 1
    return True
def res(a) :
    d = {}
    check = {}
    for value in a :
        if (nt(value)) :
            if (value not in d) :
                d[value] = 1
                check[value] = 1
            else : d[value] += 1
    for value in a :
        if (value in check and check[value]) :
            print(value,d[value])
            check[value] = 0
t = int(input())
a = [int(i) for i in input().split()]
res(a)