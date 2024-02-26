# def Min_Max (a, b , c) :
#     if (c == 1) :
#         if (a > b) : return b
#         return a
#     else : 
#         if (a > b) : return a
#         return b
# by sekido
# def res( a ) :
#    min1, min2 = 100000000 , 100000000
#    ans = 1000000000
#    for value in a :
#      if (ans > value + min1 + min2) :
#          ans = value + min1 + min2
#      if (value <= min1 ) :
#           min2 = min1
#           min1 = value
#    print(ans)
global a
test_case = int(input())
for _ in range(test_case) :
    v = input()
    a = [int(i) for i in input().split()]
    min1, min2 =  a[0] , a[1]
    ans = 1000000000
    for value in range (2,len(a) ) :
        if (ans > value + min1 + min2) :
            ans = value + min1 + min2
        if (value <= min1 ) :
            min2 = min1
            min1 = value
    print(ans)