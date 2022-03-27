# Assuming that the horizon seen from a place x meters above the ground is x(12800000+x)​ meters away, find how many meters away the horizon seen from a place H meters above the ground is.
from math import sqrt

h = int(input())

ans = sqrt(12800000 + h) * sqrt(h)
print(ans)