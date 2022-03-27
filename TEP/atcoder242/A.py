# All participants who ranked A-th or higher get a T-shirt.
# Additionally, from the participants who ranked between
# (A+1)-th and B-th (inclusive), C participants chosen uniformly at random get a T-shirt.

A, B, C, X = map(int, input().split())

if(X <= A):
    print(1.000000000000)
elif(X > A and X <= B):
    print(C/(B-A))
else:
    print(0.000000000000)