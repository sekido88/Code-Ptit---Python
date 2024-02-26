# a = [0,1,2,3,4,5,6,7,8,9,10]
def check(v) :
    if(len(v) < 3) : return False 
    for j in range(1,len(v)) :
        if (int(v[j]) > int(v[j-1])) :
            while (j < len(v) and int(v[j]) > int(v[j-1])) :
                 j = j + 1
            if (j == len(v)) : 
                return True
            else :     
                if(int(v[j]) == int(v[j-1])) : return False
                
        if (int(v[j]) < int(v[j-1])) :
            while (j < len(v) and int(v[j]) < int(v[j-1])) :
                j = j + 1
            if (j == len(v)) : 
                return True
            else : 
                return False
    return True
def solve(v) :
   if check(v) : print("YES")
   else : print("NO")
    
t = int(input())
for _ in range(t) :
    v = input()
    solve(v)