_ = input()
xs = list((map(int, input().split())))
# sort list
xs.sort()

# check if triangle is valid, viewing if the sum of the two other sides is greater than the max side
for i in range(len(xs) - 2):
    if xs[i] + xs[i + 1] > xs[i + 2]:
        print("YES")
        exit()
print("NO")