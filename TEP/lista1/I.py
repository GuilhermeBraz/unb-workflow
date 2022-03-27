"""Stan and Ollie play the game                                
of Odd Brownie Points. Some                                 
brownie points are located in the
plane, at integer coordinates. Stan
plays first and places a vertical
line in the plane. The line must
go through a brownie point and
may cross many (with the same x-
coordinate). Then Ollie places a
horizontal line that must cross a
brownie point already crossed by
the vertical line.
Those lines divide the plane
into four quadrants. The quad-
rant containing points with arbitrarily
large positive coordinates is
the top-right quadrant.
The players score according to the number of brownie points in the quadrants. If a brownie point is
crossed by a line, it doesn’t count. Stan gets a point for each (uncrossed) brownie point in the top-right
and bottom-left quadrants. Ollie gets a point for each (uncrossed) brownie point in the top-left and
bottom-right quadrants.
Your task is to compute the scores of Stan and Ollie given the point through which they draw their
lines."""


#loop while n is not 0
n = int(input())

while n != 0:
    ta = []
    ollie = stan = 0
    for i in range(n):
        #get the x and y coordinates of the brownie point
        x, y = map(int, input().split())
        ta.append((x, y))
    #calculate the quadrants
    x = ta[n // 2][0]
    y = ta[n // 2][1]

    #compare the coordinates with the lines
    for a in ta:
        if (a[0] != x and a[1] != y):
            if a[0] > x and a[1] > y or (a[0] < x and a[1] < y):
                stan += 1
            else:
                ollie += 1

    print(stan, ollie)
    #read the next n
    n = int(input())
