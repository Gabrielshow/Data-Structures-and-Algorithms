# using object representation
class Tree:
    def __init__(self, left, right):
        self.left = left
        self.right = right
        

t = Tree(Tree("a", "b"), Tree("c", "d"))
print(t.right.left)

#Multiway tree class
class Multi_Tree:
    def __init__(self, kids, next=None):
        self.kids = self.val = kids
        self.next = next
        
t = Multi_Tree(Multi_Tree("a", Multi_Tree("b", Multi_Tree("c", Multi_Tree("d")))))
print(t.kids.next.next.val)

#Bunch pattern
class Bunch(dict):
    def __init__(self, *args, **kwds):
        super(Bunch, self).__init__(*args, **kwds)
        self.__dict__ = self
        
# this pattern lets you create and set arbitrary attributes by supplying them as command-line arguments:
x = Bunch(name="Jayne Cobb", position="public Relations")
print(x.name)

# by subclassing dict, you get lots of functionality for free, such as iterating over the keys/attributes or easily checking whether an attribute is present.
Z = Bunch
z = Z(left=Z(left="a", right="b"), right=Z(left="c"))
print(z.left)
print(z.left.right)
print(z['left']['right'])
print("left" in z.right)
print("right" in z.right)

