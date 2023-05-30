class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        def traversal(node, depth):
            if node == None:
                return
            if len(res) == depth:
                res.append([])
            res[depth].append(node.val)
            traversal(node.left, depth+1)
            traversal(node.right, depth+1)
        traversal(root, 0)
        return res