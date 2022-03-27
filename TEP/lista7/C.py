# There are n points on the plane, (x1,y1),(x2,y2),…,(xn,yn).
# You need to place an isosceles triangle with two sides on the coordinate axis to cover all points
# A point is covered if it lies inside the triangle or on the side of the triangle.
# Calculate the minimum length of the shorter side of the triangle.

N = int(input())
points = list([tuple(map(int, input().split())) for _ in range(N)])

# get max of module of distance between point and origin
max_dist = max(map(lambda x: abs(x[0])+abs(x[1]), points))
print(max_dist)
