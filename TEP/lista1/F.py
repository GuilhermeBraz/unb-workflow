# Write a program that determines whether a figure, drawn with dots, is left-right symmetric or not.
# The dots are all distinct

def medium_dot(a, b):
    return ((a[0] + b[0]) / 2, (a[1] + b[1]) / 2)

#number of test cases
t = int(input())
for k in range(t):
    #number of dots
    n = int(input())
    #get dots
    dots = []
    for i in range(n):
        x, y = map(int, input().split())
        dots.append((2*x,y))

    #get median of max an min x
    mid = (max(dots, key=lambda x: x[0])[0] + min(dots, key=lambda x: x[0])[0]) / 2

    for dotCompare in dots:
        flag = False
        for dot in dots:
            if dotCompare[1]==dot[1] and (dotCompare[0]+dot[0] == mid/2):
                flag = True
                break
        if not flag:
            break
    
    if flag:
        print("YES")
    else:
        print("NO")