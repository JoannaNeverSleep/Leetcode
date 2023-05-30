import collections
class Solution:
    ''' 递归'''
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        if root.left and not root.right:
            return 1 + self.minDepth(root.left)
        if root.right and not root.left:
            return 1 + self.minDepth(root.right)
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
    
    '''迭代: 层序遍历'''
    def minDepth(self, root: Optional[TreeNode]) -> int:
        que = collections.deque([root])
        depth = 0
        while que:
            depth += 1
            size = len(que)
            for _ in range(size):
                node = que.popleft()
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
                if not node.left and not node.right:
                    return depth
        return depth