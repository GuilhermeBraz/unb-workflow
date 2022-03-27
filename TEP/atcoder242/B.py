# You are given a string S. Find the lexicographically smallest string S′ obtained by permuting the characters of S.
# Here, for different two strings s=s1​s2​…sn​ and t=t1​t2​…tm​, s<t holds lexicographically when one of the conditions below is satisfied.
# There is an integer i (1≤i≤min(n,m)) such that si​<ti​ and sj​=tj​ for all integersj (1≤j<i).
# si​=ti​ for all integers i (1≤i≤min(n,m)), and n<m.

S = input()

#find the lexicographically smallest string
# for i in range(len(S)):
    # for j in range(i+1, len(S)):
        # if(S[i] > S[j]):
            # S = S[:i] + S[j] + S[i+1:j] + S[i] + S[j+1:]
            # break
# print(S)
SS = sorted(S)
SS = "".join(SS)
print(SS)