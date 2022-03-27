n = int(input())
stars = list([tuple(map(int, input().split())) for _ in range(n)])
triangle = []
i = 0
# form triangle with the stars, so that the rest are strictly outside the triangle
while len(triangle) < 3:
    for star in stars[i:]:
        if len(triangle) == 3:
            break
        if triangle == []:
            triangle.append(star)
        else:
            # check if star is inside the triangle
            if 0:
                continue
            else:
                triangle.append(star)
    i += 1

print(triangle)
