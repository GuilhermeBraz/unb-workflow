from math import sqrt, fabs

n, r = map(int, input().split())
# xs = list(map(int, input().split()))
# ans = [r for _ in range(n)]
pos = [[float(x)for x in input().split(' ')], [r]*n]
# print(pos)
for i in range(n):
    maxp = pos[1][i]
    for j in range(i):
        mind = fabs(pos[0][i] - pos[0][j])
        if mind <= 2*r:
            maxp = max(maxp, pos[1][j]+sqrt(4*r**2-mind**2))
    pos[1][i] = maxp
print(" ".join(map(str, pos[1])))
