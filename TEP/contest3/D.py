# Vasya owns a cornfield which can be defined with two integers nnn and ddd. The cornfield can be represented as rectangle with vertices having Cartesian coordinates (0,d),(d,0),(n,n−d)(0, d), (d, 0), (n, n - d)(0,d),(d,0),(n,n−d) and (n−d,n)(n - d, n)(n−d,n).
# An example of a cornfield with n=7  and d=2
# Vasya also knows that there are m grasshoppers near the field (maybe even inside it). The i-th grasshopper is at the point (xi,yi)(x_i, y_i)(xi​,yi​). Vasya does not like when grasshoppers eat his corn, so for each grasshopper he wants to know whether its position is inside the cornfield (including the border) or outside.
# Help Vasya! For each grasshopper determine if it is inside the field (including the border).

n, d = map(int, input().split())
#get m number of grasshoppers
m = int(input())

#get the coordinates of the grasshoppers
for i in range(m):
    x, y = map(int, input().split())
    if (x+y-d>=0) and (x-y-d)<=0 and (x+y-2*n+d)<=0 and (x-y+d)>=0:
        print("YES")
    else:
        print("NO")
    