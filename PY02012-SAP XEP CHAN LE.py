def Rev(x) :
    return -x
n = int(input())
a = []
i = 0
while (i != n) :
    v = [int(i) for i in input().split()]
    for x in v :
        a.append(x)
    i += len(v)

arr_Chan = [x for x in a if x % 2 == 0]
arr_Le = [x for x in a if x % 2 != 0]

arr_Chan.sort()
arr_Le.sort( key = Rev )
u = 0
v = 0
for i in a :
    if (i & 1 and len(arr_Le) >= 1) :
        print(arr_Le[u],end = " ")
        u += 1
    elif (not(i & 1) and len(arr_Chan) >= 1) :
        print(arr_Chan[v],end = " ")
        v += 1 