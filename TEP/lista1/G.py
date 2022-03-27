#  We have to find out the length of the shortest and longest boundary distance from
# the batsman. We know the radius of the circular stadium and the
# position of the batsman.
# Center of the stadium is always the origin (0, 0).
# Boundary means the perimeter of the circular field
from math import sqrt
#number of test cases
t = int(input())
for k in range(t):
    x,y,r = map(int, input().split())
    #get the distance from the origin to the batsman
    d = sqrt(x**2 + y**2)
    #get the max boundary
    maxBoundary = r + d
    #get the min boundary
    minBoundary = r-d
    #print the result with 2 decimal places
    print("%.2f %.2f" % (minBoundary, maxBoundary))