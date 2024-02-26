ans = 0
n = input()
while (len(n) > 1) :   
        s = 0
        ans += 1
        for i in n :
            s = s + (ord(i) - 48)
        n = str(s)
print(ans)