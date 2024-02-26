def t(s,a,b,c,n) :
    if(len(s) == n and a <= b and b<=c and a > 0)  :
        print(s)
        return
    if(len(s) < n) :
        t(s + 'A' , a + 1 , b , c, n)
        t(s + 'B' , a , b + 1 , c, n)
        t(s + 'C' , a , b , c + 1 , n)
n = int(input())
for i in range(3,n + 1) :
    t("",0,0,0,i)