import sys
n = int(input())

for i in range(n):
    x = int(input())
    #if x / 4 gives rest 0, then the polygon is beautiful
    if (x%4 == 0):
        print('YES')
    else:
        print('NO')
        