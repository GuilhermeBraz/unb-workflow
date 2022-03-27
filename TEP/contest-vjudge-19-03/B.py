# A shop sells N kinds of fruits, Fruit 1,…,N, at prices of p1,…,pn, yen per item, respectively. (Yen is the currency of Japan.)
# Choose K kinds of fruits and buy one of each chosen kind. Find the minimum total price of those fruits.

N, K = map(int, input().split())
p = list(map(int, input().split()))

ans = 0
# sort list
p.sort()
for i in range(K):
    ans += p[i]
print(ans)
