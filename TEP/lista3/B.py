# Given are integers a, b, c and d.
# If x and y are integers and a <= x <=b and c <= y <= d, what is the maximum value of (x*y)?

a, b, c, d = map(int, input().split())


#get both maxs values
max_x = max(a,b)
max_y = max(c,d)

#get both mins values
min_x = min(a,b)
min_y = min(c,d)

#check if there is two negative values on each side
if (a < 0 or b < 0) and (c < 0 or d < 0):
    if(min_x * min_y > max_x * max_y):
        print(min_x * min_y)
    else:
        print(max_x * max_y)
elif (max_x > 0 and max_y < 0):
    print(min(a,b)*max_y)
elif (max_x < 0 and max_y > 0):
    print(max_x*min(c,d))
elif (max_x < 0 and max_y < 0):
    print(min(a,b)*min(c,d))
else:
    print(max_x*max_y)
