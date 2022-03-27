# With a takoyaki machine, he can make at most X pieces of takoyaki at a time, taking T minutes regardless of the number of pieces to make.
# How long does it take to make N takoyaki?

N, X, T = map(int, input().split())

#Calculate how much time it takes to make N pieces of takoyaki
if(N == 0):
    print(0)
elif(N%X==0):
    print(N//X * T)
else:
    print((N//X +1)* T)