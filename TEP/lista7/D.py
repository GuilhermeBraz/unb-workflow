# You've got a rectangular parallelepiped with integer edge lengths. You know the areas of its three faces that have a common vertex.
# Your task is to find the sum of lengths of all 12 edges of this parallelepiped.
from math import sqrt
x, y, z = map(int, input().split())

perimeter = (4*sqrt((x*y)/z)) * (1+z/x+z/y)
print(round(perimeter))
