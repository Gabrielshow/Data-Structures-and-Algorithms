A = [7, 8, 9, 0, 5, 8, 6, 1]
n = len(A)
# result = max((A[i:j] for i in range(n) for j in range(i+1,n+1)), key=sum)
result = max((A[i:j] for i in range(n) for j in range(i+1,n+1)), key=sum)
print(result)

best = A[0]
for size in range(1, n+1):
    cur = sum(A[:size])
    for i in range(n-size):
        cur += A[i+size] - A[i]
        best = max(best, cur)
print(best)

# There's a ton of different tree structures and balancing methods, but they're generally based on two fundamental operations:
# Node splitting(and merging). Nodes are allowed to have more than two children(and more tahn one key), and under certain circumstances, a node can become overfull, it is the split
# into two nodes(potentially making its parent overfull.
# Node rotations. Here we still use binary trees, but we switch edges. if x is the parent of y, we now make y the parent of x. For this to work, x must take over one of the children of y.
# for the node splitting let's consider a structure called the 2-3-tree. in a plain binary tree, each node can have up to two children,
# and they each have a single key. In a 2-3 tree,though, we allow a node to thave one or two keys and up to three children.
# Anything in the left subtree now has to be smaller than the smallest of the keys, and anything in the right subtree is greater than the greatest of the keys- and anything in the middle subtree must fall between the two
# the 2-3 tree is a special case of the B tree, which forms the basis of almost all database systems, and disk-based trees used in such diverse areas as geographic information systems and image retrieval. the important extension is that B-trees
# can have thousands of keys(and subtrees), and each node is usually stored as a contiguous block on disk.
# the main motivation for the large blocks is to  minimize the number of idsk accesses.
# right rotation is called a skew
# left rotation is called a split in balancing AA tree
# Binary Search Tree, Now with AA-Tree balancing
class Node:
    lft = None
    rgt = None
    lvl = 1
    def __init__(self, key, val):
        self.key = key
        self.val = val
        
def skew(node):
    if None in [node, node.lft]: return node
    if node.lft.lvl != node.lvl: return node
    lft = node.lft
    node.lft = lft.rgt
    lft.rgt = node
    return lft

def split(node):
    if None in [node, node.rgt, node.rgt.rgt]: return node
    if node.rgt.rgt.lvl != node.lvl: return node
    rgt = node.rgt
    node.rgt = rgt.lft
    rgt.lft = node
    rgt.lvl += 1
    return rgt

def insert(node, key, val):
    if node is None: return Node(key, val)
    if node.key == key: node.val = val
    elif key < node.key:
        node.lft = insert(node.lft, key, val)
    else:
        node.rgt = insert(node.rgt, key, val)
    node = skew(node)
    node = split(node)
    return node


