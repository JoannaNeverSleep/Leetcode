class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        
        # 判断是否为满二叉树
        leftDepth = 1
        rightDepth = 1
        cur = root
        while cur.left:
            cur = cur.left
            leftDepth += 1
        cur = root
        while cur.right:
            cur = cur.right
            rightDepth += 1
        
        if leftDepth == rightDepth:
            return 2**leftDepth - 1
        
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        