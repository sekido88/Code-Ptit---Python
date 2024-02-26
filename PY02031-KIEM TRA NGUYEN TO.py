#by sekido
def nt( x) :
    if (x < 2) : return False
    i = 2
    while(i * i <= x) :
        if (x % i == 0) :
            return False
        i += 1
    return True
m = [int(i) for i in input().split()]
v = []
for i in range(m[0]) :
    a = [int(i) for i in input().split()]
    v.append(a)

for i in range(m[0]) :
    for j in range(m[1]) :  
        if(nt(v[i][j])) : v[i][j] = 1
        else : v[i][j] = 0
        
for i in range(m[0]) :
    for j in range(m[1]) :  
        print(v[i][j],end=" ")
    print()