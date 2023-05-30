class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    # preorder
    def preorder_traversal(self,root):
        nonlocal res

        # 停止条件
        if not root:
            return 
        
        #单层逻辑
        res.append(root.val) # 中
        self.preorder_traversal(root.left)
        self.preorder_traversal(root.right)
        
    def preorderTraversal(self, root):
        res = []
        self.preorder_traversal(root)
        return res
    
    # inorder
    def inorder_traversal(self, root):
        nonlocal res
        if root == None:
            return
        self.preorder_traversal(root.left)
        res.append(root.val)
        self.preorder_traversal(root.right)

    def inorderTraversal(self, root):
        res = []
        self.inorder_traversal(root)
        return res
    
    # postorder
    def postorder_traversal(self, root):
        nonlocal res
        if not root:
            return
        self.postorder_traversal(root.left)
        self.postorder_traversal(root.right)
        res.append(root.val)
    
    def postorderTraversal(self, root):
        res = []
        self.postorder_traversal(root)
        return res