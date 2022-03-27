# First, Takahashi chooses an integer between A and B (inclusive) and tells it to Aoki.
# Next, Aoki chooses an integer between C and D (inclusive).
# If the sum of these two integers is a prime, then Aoki wins; otherwise, Takahashi wins.
def isPrime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if(n%i == 0 or n %(i+2)==0):
            return False
        i = i + 6
    
    return True


a,b,c,d = map(int, input().split())

#check if the sum of a and c is prime
if(isPrime(a+c) or isPrime(b+d)):
    print("Aoki")
else:
    print("Takahashi")