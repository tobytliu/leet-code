class Node:
    def __init__(self, val=None, right=None, left=None):
        self.val = val
        self.left = left
        self.right = right
    def __string__(self):
        return str(self.val)

result = []
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

d.left = b
d.right = f
b.left = a
b.right = c
f.left = e

def iterative_preorder(root, result):
    stack = []
    while root is not None or len(stack) > 0:
        while (root is not None):
            result.append(root)
            stack.append(root)
            root = root.left
        root = stack.pop()
        root = root.right

def iterative_inorder(root, result):
    stack = []
    while root is not None or len(stack) > 0:
#         if root is not None:
#             print(root.val, [node for node in stack])
        while (root is not None):
            stack.append(root)
            root = root.left
        root = stack.pop()
        result.append(root)
        root = root.right

iterative_preorder(d, result)

for node in result:
    print(node.val, end="")
print()
