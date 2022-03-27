t = int(input())

for i in range(t):
    a = int(input())
# n = 180/360-a
    if 360 % (180 - a) == 0:
        print('YES')
    else:
        print('NO')
