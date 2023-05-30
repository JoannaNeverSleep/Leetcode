class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def getDepth(root):
            if not root:
                return 0
            
            leftDepth = getDepth(root.left)
            if leftDepth == -1:
                return -1
            rightDepth = getDepth(root.right)
            if rightDepth == -1:
                return -1
            
            return -1 if abs(leftDepth - rightDepth) > 1 else 1 + max(leftDepth, rightDepth)
        
        return False if getDepth(root) == -1 else True