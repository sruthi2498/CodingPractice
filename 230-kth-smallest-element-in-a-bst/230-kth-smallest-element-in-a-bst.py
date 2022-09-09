# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self):
        self.inorderList=[]
    
    def inorder(self, root: Optional[TreeNode]) :
        if not root:
            return 
        if root.left:
            self.inorder(root.left)
        self.inorderList.append(root.val)
        if root.right:
            self.inorder(root.right)
        
        
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.inorder(root)
        return self.inorderList[k-1]