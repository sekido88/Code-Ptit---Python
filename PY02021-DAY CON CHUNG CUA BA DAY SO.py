def bin_sear(arr , x) :
    l = 0 
    r = len(arr) - 1
    while(l <= r) :
        m = (l + r)//2
        if (arr[m] == x) :
            return True
        elif arr[m] > x : r = m - 1
        else : l = m + 1
    return False

def res (a, b, c) :
    ok = 0
    for i in a :
        if (bin_sear(b,i) and bin_sear(c,i)) :
            print(i,end = " ")
            ok = 1
    if (ok == 0) : print("NO")
    else : print()

def res2(a,b,c) :
    ok = 0
    d = {x : 1 for x in a}
    d2 = {x : 2 for x in b} 
    for i in c :
        if (i in d and i in d2) :
            ok = 1
            print(i,end = " ")
    if (ok == 0) : print("NO")
    else : print()

def find_common_elements(arr1, arr2, arr3):
    common_elements = []
    i = j = k = 0

    while i < len(arr1) and j < len(arr2) and k < len(arr3):
        if arr1[i] == arr2[j] == arr3[k]:
            common_elements.append(arr1[i])
            i += 1
            j += 1
            k += 1
        elif arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr3[k]:
            j += 1
        else:
            k += 1
    if (len(common_elements) == 0) : 
        print("NO")
        return
    
    for i in common_elements :
        print(i,end = " ")
    print()
for _ in range(int(input())) :
    n , m , k = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    c = [int(i) for i in input().split()]
    res (a,b,c)
