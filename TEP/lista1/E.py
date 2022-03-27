# Diamond Miner is a game that is similar to Gold Miner, but there are nnn miners instead of 111 in this game.
# The mining area can be described as a plane. The nnn miners can be regarded as nnn points on the y-axis. There are nnn diamond mines in the mining area. We can regard them as nnn points on the x-axis. For some reason, no miners or diamond mines can be at the origin (point (0,0)(0, 0)(0,0)).
# Every miner should mine exactly one diamond mine. Every miner has a hook, which can be used to mine a diamond mine. If a miner at the point (a,b)(a,b)(a,b) uses his hook to mine a diamond mine at the point (c,d)(c,d)(c,d), he will spend (a−c)2+(b−d)2\sqrt{(a-c)^2+(b-d)^2}(a−c)2+(b−d)2
# ​ energy to mine it (the distance between these points). The miners can't move or help each other.
# The object of this game is to minimize the sum of the energy that miners spend. Can you find this minimum
from math import sqrt
def dis(a, b):
    return sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)
# Number of test cases
t = int(input())

for i in range(t):
    energysum = 0
    # Number of miners and diamonds - n
    n = int(input())
    miners = []
    diamonds = []

    for j in range(2*n):
        # Miner position
        x, y = map(int, input().split())
        if x == 0:
            miners.append((abs(x), abs(y)))
        else:
            diamonds.append((abs(x), abs(y)))
    
    # Sort the diamonds by their x-coordinate and the miners by the y-coordinate
    miners.sort(key=lambda x: x[1])
    diamonds.sort(key=lambda x: x[0])

    for miner,diamond in zip(miners, diamonds):
        energysum += dis(miner, diamond)

    print(energysum)
