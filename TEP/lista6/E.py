import math
# euclidean distance
# def euclidean_distance(x1, y1, x2, y2):
# return ((x1 - x2)**2 + (y1 - y2)**2)**0.5


t = int(input())
for i in range(t):
    n, distance = map(int, input().split())
    fav_numbers = list(map(int, input().split()))

    if distance in fav_numbers:
        print(1)
    elif max(fav_numbers) > distance:
        print(2)
    else:
        print(math.ceil(distance/max(fav_numbers)))
