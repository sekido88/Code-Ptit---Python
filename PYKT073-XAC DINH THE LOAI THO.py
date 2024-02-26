#by sekido 
def res(a) :
    a.append("1 2 3 4")
    ans = []
    kq = 0
    i = 0
    while(i< len(a)) :
            x = a[i].split()
            
            if ( len(x) == 6 or len(x) == 8) : 
                while(len(x) == 6 or len(x) == 8) :
                    x = a[i].split()
                    i += 1
                i = i - 1
                ans.append(1)

            if ( len(x) == 7) : 
                while(len(x) == 7 and kq != 4) :
                    x = a[i].split()  
                    i += 1    
                    kq += 1  
                i = i - 1   
                kq = 0 
                ans.append(2)
            i += 1
    print(len(ans))
    for i in ans :
        print(i)
t = int(input())
a = []
while( t > 0 ) :
    s = input()
    a.append(s)
    t -= 1
res(a)
