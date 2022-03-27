import math
R, d = map(int, input().split())
n = int(input())
ans = 0
for i in range(n):
    x, y, r = map(int, input().split())
    # check if point lands on crust of the circle
    if x**2 + y**2 >= (R-d+r)**2 and x**2 + y**2 <= (R-r)**2:
        ans += 1

print(ans)
