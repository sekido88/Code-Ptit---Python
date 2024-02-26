def Fmax( a , b) :
      if (a > b) : return a
      return b
def Fmin( a , b) :
      if (a < b) : return a
      return b

m , n = [int(i) for i in input().split()]
v = []
for i in range(m) :
    a = [int(i) for i in input().split()]
    v.append(a)

mx = 0
mn = 100000000
ok = 0
for i in range(m) :
        mx = max (mx,max (v[i]) )
        mn = min (mn, min (v[i]) )
bkey = mx - mn
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
