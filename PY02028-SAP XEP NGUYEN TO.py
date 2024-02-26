#by sekido
def nt(x) :
    i = 2
    while(i * i <= x) :
        if (x % i == 0) :
            return False
        i += 1
    return (x >= 2) 
n = int(input())
a = [int(i) for i in input().split()]
res = []
for i in range(n) :
    if (nt(a[i])) :
        res.append(a[i])
res.sort()
j = 0 
for k in range(n) :
    if (not(nt(a[k]))) :
        print(a[k],end = " ")
    else :
        print(res[j],end = " ")
        j+=1 
