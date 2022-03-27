from math import sqrt
N = int(input())

#check if N is a perfect square
sq = int(sqrt(N))
if sq*sq == N:
    print(sq*4)
else:
    r = N//sq
    p = 2*(sq+r)

    if(N%sq!=0):
        p += 2
    print(p)

