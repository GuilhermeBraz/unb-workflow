from math import sqrt

_ = input()

xs = list(map(int, input().split()))

#get absolute values
xs = list(map(abs, xs))

#manhattan distance ∣x1∣+…+∣xN∣
manhattan = sum(xs)

#euclidian distance √(∣x1∣)^2+…+∣xN∣
euclidian = sqrt(sum(map(lambda x: x**2, xs)))

#chebyshev distance max(∣x1∣,…,∣xN∣)
chebyshev = max(xs)

print(f'{manhattan}\n{euclidian}\n{chebyshev}')