from binary_tree import Tree_Node

class Solution:
    def isValidBST(self, root) -> bool:
        res = []
        self.inOrderTraverse(root, res)
        for i in range(len(res) - 1):
            if res[i] >= res[i + 1]:
                return False
        return True
    def inOrderTraverse(self, root, res):
        if root:
            inOrderTraverse(root.left)
            res.append(root.val)
            inOrderTraverse(root.right)
