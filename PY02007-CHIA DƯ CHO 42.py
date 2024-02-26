#by sekido
count  = 0
v = []
while(True) :
    a = [int(i) for i in input().split()]
    for i in a :
        v.append(i)
    count += len(a)
    if (count == 10) : break
d = {}
for i in v :
    d[int(i%42)] = 0
    # print(int(i%42))
print(len(d))