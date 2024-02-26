def res(s,k) :
    p = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
    dd = {} 
    for i in range(len(p)) :
        dd [p[i]] = p[(i + k)%28] 
    res = ""
    for i in s:
        res = str(dd[i]) + res
    print(res)
while(True) :
    y = input()
    if(y == '0') : break
    x = y.split()
    k = int(x[0])
    s = str(x[1])
    res(s,k)