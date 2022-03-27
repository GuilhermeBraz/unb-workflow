t = int(input())
for i in range(t):
    r = int(input())
    length = r*5
    width = length*0.6
    left = -1*length*0.45
    right = length*0.55
    w = width/2
    # print coordinates
    print('Case '+str(i+1)+':')
    # upper left
    print("%.0f %.0f" % (left, w))
    # upper right
    print("%.0f %.0f" % (right, w))
    # lower right
    print("%.0f %.0f" % (right, -1*w))
    # lower left
    print("%.0f %.0f" % (left, -1*w))
