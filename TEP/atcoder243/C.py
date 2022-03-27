'''
There are N people in an xy-plane. Person i is at (Xi​,Yi​). The positions of all people are different.
We have a string S of length N consisting of L and R.
If Si​= R, Person i is facing right; if Si​= L, Person i is facing left. All people simultaneously start walking in the direction they are facing. 
Here, right and left correspond to the positive and negative x-direction, respectively.
We say that there is a collision when two people walking in opposite directions come to the same position.
Will there be a collision if all people continue walking indefinitely?
'''
#Constraints
'''
2≤N≤2×105
0≤Xi​≤109
0≤Yi​≤109
(Xi​,Yi​)=(Xj​,Yj​) if
i=j.
All
Xi​ and
Yi​ are integers.
S is a string of length N consisting of L and R.
'''
Y = []
N = int(input())
for i in range(N):
    x,y = map(int, input().split())
    Y.append(y) 
S = input()
if not('R' in S) or not('L' in S):
    print('No')
else:
    i = 0
    for i in range(N):
       for j in range(N):
            if(Y[i] == Y[j]) and (S[i] != S[j]):
                # print((Y[i],Y[j]))
                # print((i,j))
                print('Yes')
                exit()
    print('No')