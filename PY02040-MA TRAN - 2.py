#by sekido
n = int(input())
v = []
for i in range(n) :
    a = [int(i) for i in input().split()]
    v.append(a)
st = 0
sd = 0
sc = 0
for i in range(n ) :
    for j in range(n - i - 1) :
        st += v[i][j]
        sd += v[n - i - 1][n - j - 1]
k = int(input())
# print(st)
# print(sd)
cc = abs(st - sd)
if (cc <= k ) :
    print("YES")
    print(cc) 
else : 
    print("NO")
    print(cc)