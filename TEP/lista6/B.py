# number of sides
N = int(input())
T = list(map(int, input().split()))
ans = 0

# check how many triples makes a triangle
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if T[i] != T[j] and T[i] != T[k] and T[j] != T[k]:
                if T[i] + T[j] > T[k] and T[i] + T[k] > T[j] and T[j] + T[k] > T[i]:
                    ans += 1
print(ans)
