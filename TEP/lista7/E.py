import math
N, Sx, Sy = map(int, input().split())

xs = list([tuple(map(int, input().split())) for _ in range(N)])

a = b = c = d = 0

for x, y in xs:
    if x == Sx:
        if y < Sy:
            d += 1
        elif y > Sy:
            b += 1
        continue
    else:
        if x < Sx:
            a += 1
        else:
            c += 1
        if(y == Sy):
            continue

    if y == Sy:
        if x > Sx:
            c += 1
        elif x < Sx:
            a += 1
        continue
    else:
        if y < Sy:
            d += 1
        else:
            b += 1

students = max(a, b, c, d)
print(students)
if students == a:
    print(Sx-1, Sy)
elif students == b:
    print(Sx, Sy+1)
elif students == c:
    print(Sx+1, Sy)
else:
    print(Sx, Sy-1)
