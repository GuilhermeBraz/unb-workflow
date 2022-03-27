# DLS and JLS are bored with a Math lesson. In order to entertain themselves, DLS took a sheet of paper and drew n distinct lines, given by equations y=x+piy = x + p_iy=x+pi​ for some distinct p1,p2,…,pnp_1, p_2, \ldots, p_np1​,p2​,…,pn​.
# Then JLS drew on the same paper sheet m distinct lines given by equations y=−x+qiy = -x + q_iy=−x+qi​ for some distinct q1,q2,…,qmq_1, q_2, \ldots, q_mq1​,q2​,…,qm​.
# DLS and JLS are interested in counting how many line pairs have integer intersection points, i.e. points with both coordinates that are integers. Unfortunately, the lesson will end up soon, so DLS and JLS are asking for your help.

#number of test cases
t = int(input())

for i in range(t):
    #number of lines
    #dls
    n = int(input())
    dls = list(map(int, input().split()))
    #jls 
    m = int(input())
    jls = list(map(int, input().split()))

    #calculate the intersection points
    intersection = 0
    for p in dls:
        for q in jls:
                if (p-q)==0 or (p-q)%2 == 0:
                    intersection += 1
    print(intersection)