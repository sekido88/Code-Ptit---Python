n = int(input()) 
a = [int(i) for i in input().split()]
res = 0
value = 0
ans = 1e9
for i in range(n) :
    value = a[i] 
    tmp = 0
    for j in range(n) :
        tmp += abs(a[j] - a[i])
        # res = max (res , tmp )
    if (ans > tmp) :
        # print(a[i])
        res = a[i]
        ans = tmp
print(ans,res)