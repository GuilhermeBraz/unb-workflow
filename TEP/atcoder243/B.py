N = int(input())
sum1 = 0
sum2 = 0

A = list(map(int, input().split()))
B = list(map(int, input().split()))
#check number of equals in A and B
for a,b in zip(A,B):
    if a == b:
        sum1 += 1
#check number of equals pairs with different index in A and B
for a in A:
    #get index of a
    index = A.index(a)
    for b in B:
        if a == b and index != B.index(b):
            sum2 += 1
print(sum1)
print(sum2)
    