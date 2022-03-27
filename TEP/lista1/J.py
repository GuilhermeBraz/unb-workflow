"""You should write a program to check whether the two parts of a port match. The pins (and holes)
of the plug (socket) are given to you as a set of N distinct points in 2D plane. You can translate the
points in a set altogether. You can also rotate them around the origin in mul pliers of 90 degrees.
(i.e. 90, 180 or 270 degrees) Two parts match each other if a one to one correspondence can be made
between the points of the two sets using translation and rotation."""

#number of test cases
t = int(input())
for i in range(t):
    #number of points
    n = int(input())
    #get points
    points = []
    for i in range(n):
        x, y = map(int, input().split())
        points.append((x,y))
    #get median of max an min x
    mid = (max(points, key=lambda x: x[0])[0] + min(points, key=lambda x: x[0])[0]) / 2
    #get median of max an min y
    mid2 = (max(points, key=lambda x: x[1])[1] + min(points, key=lambda x: x[1])[1]) / 2
    #get the points of the first part
    points1 = []
    for point in points:
        if point[0] <= mid:
            points1.append(point)
    #get the points of the second part
    points2 = []
    for point in points:
        if point[0] > mid:
            points2.append(point)
    #sort the points of the first part by their y-coordinate
    points1.sort(key=lambda x: x[1])
    #sort the points of the second part by their y-coordinate
    points2.sort(key=lambda x: x[1])
    #check if the two parts match
    for point1, point2 in zip(points1, points2):
        if point1[1] != point2[1]:
            print("NO")
            break
    else:
        print("YES")