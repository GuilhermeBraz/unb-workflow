import math
# We will buy a product for N yen at a shop.
# If we use only 1000-yen bills to pay the price, how much change will we receive?
# Assume we use the minimum number of bills required.

# Get the price of the product
N = int(input())

# get number of bills
bills = math.ceil(N/1000)

# calculate change
change = bills * 1000 - N

print(change)
