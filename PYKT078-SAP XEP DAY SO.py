#by sekido 
def res( a , k) :
    mx_v = max(a)
    mx_p = 0
    am = []
    a0 = []
    duong = []
    for i in range(len(a)) :
        if (a[i] == mx_v and mx_p == 0 ) :
           mx_p = i
           continue
    a.insert(mx_p  , k)
    for i in range(len(a)) :
        if (a[i] < 0) : 
           am.append(a[i])
        # elif (a[i] == 0) :
        #     a0.append(0)
        else : 
            duong.append(a[i])
    for i in am :
        print(i,end = " ")
    # for j in a0 :
    #     print(j,end = " ")
    for u in duong :
        print(u,end = " ")
    print()
t = int(input())
while(t>0) :
    n , k = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    res(a,k)
    t -= 1