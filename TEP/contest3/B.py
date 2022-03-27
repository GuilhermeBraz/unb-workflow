# Vasiliy lives at point (a, b) of the coordinate plane. He is hurrying up to work so he wants to get out of his house as soon as possible. New app suggested n available Beru-taxi nearby. The i-th taxi is located at point (xi, yi) and moves with a speed vi.
# Consider that each of n drivers will move directly to Vasiliy and with a maximum possible speed. Compute the minimum time when Vasiliy will get in any of Beru-taxi cars.
from  math import sqrt
a, b = map(int, input().split())

#get number of taxies
n = int(input())
time = []
for i in range(n):
    x, y, v = map(int, input().split())
    #check the taxi with the shortest arrival time
    #check distance between Vasiliy and taxi
    distance = sqrt(abs(a - x)**2 + abs(b - y)**2)
    #check the time when the taxi will arrive
    time.append (distance / v)

print(min(time))