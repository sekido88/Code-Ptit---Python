def Anal_Pr(max_value) :
    i = 2
    const_N = max_value + 10
    global anal_pr
    anal_pr = [0] * const_N
    while(i<= const_N - 1) :
        if (anal_pr[i] == 0) :
            for j in range(i+i,const_N,i) :
                anal_pr[j] += i + anal_pr[j//i]
                if (anal_pr[j//i] == 0) : anal_pr[j] += i
        i += 1
    for j in range(1,const_N) :
        if (anal_pr[j] == 0) : 
            anal_pr[j] = j

# def sum(x) :
#     ans = 0 
#     while(x != 1 and x > 0) :
#         ans += anal_pr[x]
#         x = x // anal_pr[x]
#     return ans

def max( a , b) :
    if (a > b ) : return a
    return b

ans = 0
max_e = 0
t = int(input())
v = []

for _ in range(t) :
    x = int(input())
    v.append(x)
    max_e = max(x, max_e)
Anal_Pr(max_e)

for i in v :
    # ans += sum(i)
    print(anal_pr[i]) 
print(ans)
