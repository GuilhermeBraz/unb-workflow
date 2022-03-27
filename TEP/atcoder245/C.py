# You are given two sequences, each of length N, consisting of integers: A=(A1​,…,AN​) and B=(B1​,…,BN​).
# Determine whether there is a sequence of length N, X=(X1​,…,XN​), satisfying all of the conditions below.
# Xi​=Ai​ and Xi​=Bi​, for every i(1≤i≤N). ∣Xi​−Xi+1​∣≤K, for every i(1≤i≤N−1).

N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# check if there is an X list that satisfies the conditions
# for a, b in zip(A, B):
# get a index
# index = A.index(a)
# for ac, bc in zip(A[index:], B[index:]):
# if abs(a - bc) <= K and abs(a - ac) <= K and abs(b - bc) <= K:
# continue
# else:
# print('No')
# exit()
# print('Yes')

