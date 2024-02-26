# by sekido
def solve(v, n) :
    ans = 0
    len_n = len(n)
    len_v = len(v)
    i = 0
    while ( i < len_v ) :
      if ( i + len_n > len_v) : break
      number = v[i : i + len_n]
      if (number == n) : 
        ans += 1
        i = i + len_n 
        continue
      i += 1  
    print(ans)
    
t = int(input())
for _ in range(t) :
    v = str(input())
    n = str(input())
    solve(v, n)
    # print(v[1:5])