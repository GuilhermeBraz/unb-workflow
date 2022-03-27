# Argus was charged with guarding Io, which is not an ordinary cow. Io is quite an explorer, and she wanders off rather frequently, making Argus' life stressful. So the cowherd decided to construct an enclosed pasture for Io.
# There are nnn trees growing along the river, where Argus tends Io. For this problem, the river can be viewed as the OXOXOX axis of the Cartesian coordinate system, and the nnn trees as points with the yyy-coordinate equal 000. There is also another tree growing in the point (0,1)(0, 1)(0,1).
# Argus will tie a rope around three of the trees, creating a triangular pasture. Its exact shape doesn't matter to Io, but its area is crucial to her. There may be many ways for Argus to arrange the fence, but only the ones which result in different areas of the pasture are interesting for Io. Calculate the number of different areas that her pasture may have. Note that the pasture must have nonzero area.

t = int(input())
for i in range(t):
    n = int(input())
    xs = list(map(int, input().split()))
    