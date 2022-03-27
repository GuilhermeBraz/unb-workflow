'''You are given a string S consisting of A, B, C.
Let S(0):=S. For i=1,2,3,…, let S(i) be the result of simultaneously replacing the characters of
S(i−1) as follows: A → BC, B → CA, C → AB.

Answer Q queries. The i-th query is as follows.
    Print the ki​-th character from the beginning of S(ti​).

Constraints
S is a string of length between 1 and 105 (inclusive) consisting of A, B, C.
1≤Q≤105
0≤ti​≤1018
1≤ki​≤min(1018, the length of S(ti​))
Q,ti​,ki​ are integers.'''

S = input()
Q = int(input())
for i in range(Q):
    ti, ki = map(int, input().split())
    print(S[ki])

    #change the A to BC, B to CA, C to AB at the same time
    S = S.replace('A', 'XC')
    S = S.replace('B', 'YA')
    S = S.replace('X', 'B')
    S = S.replace('C', 'AB')
    S = S.replace('Y', 'C')
    # print(S)
    
    