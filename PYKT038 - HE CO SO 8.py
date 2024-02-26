def tinh(s) :
    res = 0 
    sm = 2
    for i in range(3) :
        res = res + int(s[i]) * pow(2,sm)
        sm -= 1
    return res
ans = ""
s = input()
du = 0
if (len(s) % 3 != 0) : du = 3-len(s)%3
for _ in range(du) :
    s = '0' + s
for i in range(0,len(s),3) :
    ans = ans + str(tinh(s[i:i + 3]))
print(ans)