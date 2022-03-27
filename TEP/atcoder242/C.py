# Given an integer N, find the number of integers X that satisfy all of the following conditions, modulo 998244353.
'''X is an N-digit positive integer.
Let X1​,X2​,…,XN​ be the digits of X from top to bottom. They satisfy all of the following:

1≤Xi​≤9 for all integers 1≤i≤N;
∣Xi​−Xi+1​∣≤1 for all integers 1≤i≤N−1.
'''
N = int(input())


#total numbers with N between 1 and 9 that Xi - Xi+1 <= 1
T = 3**(N-1) * 8 + 1
print(T% 998244353)

11
12
21
22
23
32
33
34
43
44
45
54
55
56
65
66
67
76
77
78
87
88
89
98
99

