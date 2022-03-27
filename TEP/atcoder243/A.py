V, A, B, C = map(int, input().split())

total = V
while(total >= 0):
    if A > total:
        print('F')
    elif B > (total-A):
        print('M')
    elif C > (total-A-B):
        print('T')
    total = total - A - B - C

