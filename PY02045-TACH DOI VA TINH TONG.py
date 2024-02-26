n = input()
while (len(n) != 1) :
    a = n[:(len(n)//2)]
    b = n[ (len(n)//2) : len(n) ]
    n = int(a) + int(b)
    print(n)
    n = str(n)