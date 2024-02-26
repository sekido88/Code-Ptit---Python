def Fmax( a , b) :
      if (a > b) : return a
      return b
def Fmin( a , b) :
      if (a < b) : return a
      return b
def nt(x) :
    i = 2;
    while(i * i <= x) :
         if (x % i == 0) : return False
         i += 1
    return (x >= 2)
    
m , n = [int(i) for i in input().split()]
v = []
for i in range(m) :
    a = [int(i) for i in input().split()]
    v.append(a)

mx = 0
mn = 100000000
ok = 0
for i in range(m) :
        for j in range(n) :
              if(nt (v[i][j])) :
                   mx = max(mx,v[i][j])                    
bkey = mx
res = []
for i in range(m) :
    for j in range(n) :
          if (v[i][j] == bkey) :
                tmp = "Vi tri "+'['+str(i)+']' +"["+str(j) + "]" 
                res.append(tmp)
                ok = 1
if (ok == 0) : print("NOT FOUND")
else :
    print(bkey)
    for i in res :
          print(i)
