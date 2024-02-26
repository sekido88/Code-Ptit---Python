#by sekido
def res (a,b) :
    if ( b == 1 ) :
        if (a >= 20) :
            return "Bao Binh"
        else :
            return "Ma Ket"
    if ( b == 2 ) :
        if (a >= 19) :
            return "Song Ngu"
        else :
            return "Bao Binh"
    if ( b == 3 ) :
        if (a >= 21) :
            return "Bach Duong"
        else :
            return "Song Ngu"
    if ( b == 4 ) :
        if (a >= 20) :
            return "Kim Nguu"
        else :
            return "Bach Duong"
    if ( b == 5 ) :
        if (a >= 21) :
            return "Song Tu"
        else :
            return "Kim Nguu"
    if ( b == 6 ) :
        if (a >= 21) :
            return "Cu Giai"
        else :
            return "Song Tu"
    if ( b == 7 ) :
        if (a >= 23) :
            return "Su Tu"
        else :
            return "Cu Giai"
    if ( b == 8 ) :
        if (a >= 23) :
            return "Xu Nu"
        else :
            return "Su Tu"
    if ( b == 9 ) :
        if (a >= 23) :
            return "Thien Binh"
        else :
            return "Xu Nu"
    if ( b == 10 ) :
        if (a >= 23) :
            return "Thien Yet"
        else :
            return "Thien Binh"
    if ( b == 11 ) :
        if (a >= 23) :
            return "Nhan Ma"
        else :
            return "Thien Yet"
    if ( b == 12 ) :
        if (a >= 22) :
            return "Ma Ket"
        else :
            return "Nhan Ma"
t = int(input())
for _ in range(t) :
    x = [int (i) for i in input().split()]
    print(res(x[0],x[1]))