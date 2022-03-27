n, m = map(int, input().split())
rectangle = []
# fill the n x m map with '.' or '*'
for i in range(n):
    index = 1
    xs = input()
    # get all the '*' coordinates
    for x in xs:
        if x == '*':
            rectangle.append((i+1, index))
        index += 1
# form rectangle with the forth coordinate
x = map(lambda x: x[0], rectangle)
x = list(x)
# if element repeats remove it
x = [item for item in x if x.count(item) == 1]
# same for y
y = map(lambda x: x[1], rectangle)
y = list(y)
y = [item for item in y if y.count(item) == 1]


print(x[0], y[0])
