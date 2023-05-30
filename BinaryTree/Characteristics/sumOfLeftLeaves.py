class Solution:
    '''递归'''
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        if root.left and not root.left.left and not root.left.right:
            leftvalue = root.left.val
        return leftvalue + self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
    
    '''迭代'''
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = [root]
        leftvalue = 0
        while stack:
            node = stack.pop()
            if node.left and not node.left.left and not node.left.right:
                leftvalue += node.left.val
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return leftvalue