# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def _isBalanced(self,root):
        # print(root.val)
        if not root:
            return 0,True
        if not root.left and not root.right:
            return 1,True
        lDepth,lFlag = self._isBalanced(root.left)
        rDepth,rFlag = self._isBalanced(root.right)
        # print("\t",root.val,lDepth,lFlag,rDepth,rFlag)
        if not lFlag or not rFlag or abs(lDepth-rDepth)>1:
            return None,False
        return 1+max(lDepth,rDepth),True
        
        
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        _,flag =  self._isBalanced(root)
        return flag