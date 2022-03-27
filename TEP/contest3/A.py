# Yura is tasked to build a closed fence in shape of an arbitrary non-degenerate simple quadrilateral. He's already got three straight fence segments with known lengths aaa, bbb, and ccc. Now he needs to find out some possible integer length ddd of the fourth straight fence segment so that he can build the fence using these four segments. In other words, the fence should have a quadrilateral shape with side lengths equal to aaa, bbb, ccc, and ddd. Help Yura, find any possible length of the fourth side.
# A non-degenerate simple quadrilateral is such a quadrilateral that no three of its corners lie on the same line, and it does not cross itself.

t = int(input())

for i in range(t):
    xs = list(map(int, input().split()))
    #check if the quadrilateral is not degenerate 
    xs.sort()
    if xs[0] + xs[1] < xs[2]:
        print(xs[2] - xs[0]-2)
    else:
        print(xs[2] + xs[0])
