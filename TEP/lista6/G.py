# add coordinates
def add(a, b):
    return (a[0]+b[0], a[1]+b[1])


# check if valid flag
t = int(input())
for i in range(t):
    xs = list(map(int, input().split()))
    r = xs[6]
    cc = (xs[4], xs[5])
    length = r*5
    width = length*0.6
    left = -1*length*0.45
    right = length*0.55
    w = width/2
    # upper right
    ll = (left, -1*w)
    ur = (right, w)

    lowerLeft = (xs[0], xs[1])
    upperRight = (xs[2], xs[3])

    # sum lower left with cc
    cll = add(ll, cc)
    # sum upper right with cc
    cur = add(ur, cc)

    if lowerLeft == cll and upperRight == cur:
        print('YES')
    else:
        print('NO')
