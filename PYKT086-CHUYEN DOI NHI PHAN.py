def log2( x ) :
    for i in range(5) :
        if (2 ** i == x) : return i

def tinh(s , base) :
    tmp = "0123456789ABCDEF"
    res = 0 
    sm = base - 1
    for i in range(base) :
        res = res + int(s[i]) * pow(2,sm)
        sm -= 1
    return tmp[res] 

file = open('DATA.in','r')
for _ in range(int(file.readline())) :
    
    ans = ""
    base = log2(int(file.readline()))
    s = file.readline().rstrip('\n')
    du = 0
    if (len(s) % base != 0) : du = base-len(s)%base
    for _ in range(du) :
        s = '0' + s
    for i in range(0,len(s),base) :
        ans = ans + str(tinh( s[i:i + base] , base ))
    print(ans)