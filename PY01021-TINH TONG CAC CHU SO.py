#by sekido
def res(s ) :
    x = 0
    dd = {}
    for i in range(len(s)) :
        if (s[i] >= '0' and s[i] <= '9') :
            x = x + ord(s[i]) - 48
        else :
            if (not(s[i] in dd)) :
               dd[s[i]] = 1
            else : dd[s[i]] += 1
    dd = dict(sorted(dd.items()))
    for u , v in dd.items() :
        for k in range(int(v)) :
            print(u,end = "")
    print(x)
for _ in range( int(input())) :
# s = input()
    res(input())
        
    

