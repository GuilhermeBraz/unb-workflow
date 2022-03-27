"""We have a rooted tree with N vertices. The vertices are numbered 1 through N, and the root is Vertex 1.
The i-th edge connects Vertices Ai​ and Bi​.
Vertex i has an integer

Xi​ written on it.

You are given
Q queries. For the i-th query, given a pair of integers

(Vi​,Ki​), answer the following question.

    Question: among the integers written on the vertices in the subtree rooted at Vertex 

Vi​, find the Ki​-th largest value."""
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

#get the kth largest value
def get_kth_largest(root, k):
    if root is None:
        return None
    if k == 1:
        return root.val
    if root.left is not None:
        if get_kth_largest(root.left, k-1) is not None:
            return get_kth_largest(root.left, k-1)
    if root.right is not None:
        if get_kth_largest(root.right, k-1) is not None:
            return get_kth_largest(root.right, k-1)
    return None

n,q = map(int, input().split())
tree = []
xs = list(map(int, input().split()))
for x in xs:
    tree.append(Node(x))
# print(tree)
for i in range(n-1):
    a,b = map(int, input().split())
    tree[a-1].left = tree[b-1]

for i in range(q, 0, -1):
    get_kth_largest(tree[0], q)
