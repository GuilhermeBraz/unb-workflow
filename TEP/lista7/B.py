# Takahashi is participating in a programming contest called AXC002, and he has just submitted his code to Problem A.
# The problem has NNN test cases.
# For each test case i (1≤i≤N1\leq i \leq N1≤i≤N), you are given a string Si representing the verdict for that test case. Find the numbers of test cases for which the verdict is AC, WA, TLE, and RE, respectively.
# See the Output section for the output format.

from collections import Counter

types = ['AC', 'WA', 'TLE', 'RE']

# get input in list
xs = list([input() for _ in range(int(input()))])

# travel list counting and printing each type
for t in types:
    print(t, ' x ', xs.count(t))
