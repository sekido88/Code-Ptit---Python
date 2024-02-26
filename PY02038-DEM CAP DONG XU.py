n = int(input())
v = []
def tohop(x) :
    return ((x*(x-1))//2)
for _ in range(n) :
    x = input()
    v.append(x)
res = 0
dph = [0] * (n+1)
dpc = [0] * (n+1)
for i in range(n) :
    for j in range(n) :
        if(v[i][j] == 'C') :  dph[i] += 1
        if(v[j][i] == 'C') : dpc[i] += 1
for i in range(n) :
    res += tohop(dph[i]) + tohop(dpc[i])
print(res)