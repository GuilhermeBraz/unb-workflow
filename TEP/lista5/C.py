N = int(input())
case1 = 0
case2 = 0
# case3 = 0
# case4 = 0
for i in range(N):
    x, y = map(int, input().split())
    if x > 0 :
        case1 += 1    
    elif x < 0 :
        case2 += 1    
    # elif(x > 0 and y < 0):
        # case3 += 1
    # elif(x < 0 and y > 0):
        # case4 += 1
    else:
        print("Error")
if(N-case1 <=1 or N-case2 <=1):
    print('Yes')    
else:
    print('No')












