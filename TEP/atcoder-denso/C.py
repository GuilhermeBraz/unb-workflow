# On an xy-coordinate plane, is there a lattice point whose distances from two lattice points (x1​,y1​) and (x2​,y2​) are both 5?
# The distance between two points (a,b) and (c,d) is defined to be the Euclidean distance between them, (a−c)2+(b−d)2
def euclidean_distance(x1, y1, x2, y2):
    return sqrt(((x1 - x2) ** 2 + (y1 - y2) ** 2))
from math import sqrt
x1, y1, x2, y2 = map(int, input().split())

#All combinations of points between 0 and max(x1,x2)
points = []
for i in range(min(x1,x2) + 5, (max(x1, x2) + 1)+ 5):
    for j in range(min(y1,y2) + 5, (max(y1, y2) + 5)):
        points.append((i, j))
print(points) 

#find a point in points with distance sqrt(5) from (x1,y1)
for point in points:
    if euclidean_distance(x1, y1, point[0], point[1]) == sqrt(5) and euclidean_distance(x2, y2, point[0], point[1]) == sqrt(5):
        print("Yes")
        break
    else:
        print("No")

    # import sys
    # x1, y1, x2, y2 = map(int, input().split())
    # x = abs(x2 - x1)
    # y = abs(y2 - y1)
    # if x + y == 2:
    #   print("Yes")
    #   sys.exit(0)
    # if x == 3 and y == 1:
    #   print("Yes")
    #   sys.exit(0)
    # if x == 1 and y == 3:
    #   print("Yes")
    #   sys.exit(0)
    # if x == 3 and y == 3:
    #   print("Yes")
    #   sys.exit(0)
    # if x == 0 and y == 4:
    #   print("Yes")
    #   sys.exit(0)
    # if x == 4 and y == 0:
    #   print("Yes")
    #   sys.exit(0)
    # if x == 4 and y == 2:
    #   print("Yes")
    #   sys.exit(0)
    # if x == 2 and y == 4:
    #   print("Yes")
    #   sys.exit(0)
    # print("No")