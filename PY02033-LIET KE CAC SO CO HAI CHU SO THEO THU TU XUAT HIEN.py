s = str(input())
dd = [0] *1002
a = []
ok = 0
check = 0
if (len(s) % 2 != 0) : ok = 1
vip = 0
for i in range(0,len(s) - ok,2) :
    vip = (vip + int(s[i])) * 10 + int(s[i+1])
    if (dd[vip] == 0) :
        a.append(vip)
    dd[vip] = 1
    vip = 0
for i in a:
    print(i,end=" ")
# k = int(input())
# for i in range(1001) :
#     if(dd[i] >= k) :
#         print(i,dd[i])
#         check = 1
# if (check == 0) :
#     print("NOT FOUND")


