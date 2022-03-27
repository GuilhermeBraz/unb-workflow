# You are given a sequence of length N consisting of integers: A=(A1​,…,AN​).
# Find the smallest non-negative integer not in (A1​,…,AN​).
_ = input()
A = list(map(int, input().split()))

# remove negative numbers
A = [x for x in A if x >= 0]
# print(A)
# get smaller number that doesnt exist in A
if len(A) == 0 or 0 not in A:
    print(0)
else:
    ans = min(range(min(A), max(A)+1), key=lambda x: A.count(x))
    if ans not in A:
        print(ans)
    else:
        print(max(A)+1)
