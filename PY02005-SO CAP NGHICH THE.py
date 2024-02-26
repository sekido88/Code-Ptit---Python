
def check ( i , j , vi, vj) :
    if (i < j and vi > vj) :
        return True
    return False

v = []
ans = 0
n = int(input()) 
a = [int(j) for j in input().split()]
for k in a :
    v.append(k)

for x in range(len(v)) :
        for y in range(x+1,len(v)) :
            if( check ( x , y , v[x] , v[y])) :
                ans += 1
print(ans)