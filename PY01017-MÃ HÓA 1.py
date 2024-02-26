def res (s) :
    count = 0
    s = s+"!"
    if(s[0] == s[1]) : count += 1
    else : count = 1
    for i in range(1,len(s)) :
        if(len(s) == 2) : count = 1
        if (s [i] == s[i-1] ) :
             count += 1
             continue
        print(str(count)+s[i-1],end="")
        count = 1
    print()

t = int(input())
while (t>0) :
    s = input() 
    res(s)
    t-=1
# for t in range(int(input())):
#     s = input() + '!'
#     cnt, ch = 0, s[0]
#     for i in s:
#         if i == ch:
#             cnt += 1
#         else:
#             print(str(cnt) + ch, end='')
#             cnt, ch = 1, i
#     print()