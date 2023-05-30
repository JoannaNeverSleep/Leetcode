# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''递归Recursion'''
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def compare(left, right):
            # 首先排除空节点
            if left == None and right == None:
                return True
            elif not left:
                return False
            elif not right:
                return False
            # 排除值不相等的情况
            elif left.val != right.val:
                return False
            
            return compare(left.left, right.right) and compare(left.right, right.left) # 处理下一层
        return compare(root.left, root.right)
    
    '''迭代Iteration: queue or stack or BFS'''
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        stack = [root.left, root.right]
        while stack:
            right = stack.pop()
            left = stack.pop()
            if not left and not right:
                continue
            if not left or not right or left.val != right.val:
                return False
            # outside nodes
            stack.append(left.left)
            stack.append(right.right)
            # inside nodes
            stack.append(left.right)
            stack.append(right.left)
        return True

