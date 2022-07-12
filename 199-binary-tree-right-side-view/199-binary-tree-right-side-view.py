# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.result = []
    def _rightSideView(self, root, currentDepth) :
        # print("root",root.val,"currentDepth",currentDepth,"result",self.result)
        if currentDepth > len(self.result):
            self.result.append(root.val)
        if root.right :
            self._rightSideView(root.right, currentDepth+1)
        if root.left :
            self._rightSideView(root.left, currentDepth+1)
        
            
        
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        self._rightSideView(root,1)
        print(self.result)
        return self.result