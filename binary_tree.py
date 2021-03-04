from typing import List

class Tree_Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_traversal(root: Tree_Node) -> List[int]:
    result = []
    inorder_traversal_helper(root, result)
    return result

def inorder_traversal_helper(root: Tree_Node, result: List[int]):
    if root:
        inorder_traversal_helper(root.left, result)
        result.append(root.val)
        inorder_traversal_helper(root.right, result)

def inorder_traversal_iterative(root: Tree_Node) -> List[int]:
    res, stack = [], []
    while True:
        while root:
            stack.append(root)
            root = root.left
        if len(stack) == 0:
            return res
        node = stack.pop()
        res.append(node.val)
        root = node.right

def preorder_traversal(root: Tree_Node) -> List[int]:
    result = []
    preorder_traversal_helper(root, result)
    return result

def preorder_traversal_helper(root: Tree_Node, result: List[int]):
    if root:
        result.append(root.val)
        preorder_traversal_helper(root.left, result)
        preorder_traversal_helper(root.right, result)

def preorder_traversal_iterative(root: Tree_Node) -> List[int]:
    res, stack = [], []
    while True:
        stack
        res.append(node.val)


root = Tree_Node(4)
root.left = Tree_Node(3)
root.right = Tree_Node(5)
node = root.left
node.left = Tree_Node(1)
node.right = Tree_Node(2)

print("inorder: ", inorder_traversal(root))
print("inorder(iterative)", inorder_traversal_iterative(root))
print("preorder: ", preorder_traversal(root))
