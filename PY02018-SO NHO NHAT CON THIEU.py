d = {}
n = int(input())
a = [int(i) for i in input().split()]
ans = 0
check = 0
for i in range(1,n + 2) :
    if (not(i in a)) :
        print(i)
        break