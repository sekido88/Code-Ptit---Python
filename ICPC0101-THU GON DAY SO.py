#by sekido 
n = int(input())
a = [int(i) for i in input().split()]
res = []
i = 0
while (i < len(a)) :
    res.append(a[i])
    ok = 1
    while (len(res) >= 2 and ok == 1) :
        ok = 0
        x = res[len(res) - 1]
        y = res[len(res) - 2]
        if (x + y) % 2 == 0 : 
            res.pop()
            res.pop()
            ok = 1
    i += 1 
print(len(res))