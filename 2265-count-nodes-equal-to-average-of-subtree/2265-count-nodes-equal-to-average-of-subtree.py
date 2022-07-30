# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self):
        self.count = 0
    
    def sumAndCount(self, root):
        if not root:
            return 0,0
        if not root.left and not root.right:
            self.count+=1
            return root.val, 1
        
        leftSum,leftCount,rightSum,rightCount = 0,0,0,0
        if root.left:
            leftSum,leftCount = self.sumAndCount(root.left)
            
        if root.right:
            rightSum,rightCount = self.sumAndCount(root.right)
            
        nodeSum = leftSum+rightSum+root.val
        nodeCount = leftCount+rightCount + 1
        # print("root",root.val,"nodeSum",nodeSum,"nodeCount",nodeCount)
        if nodeSum//nodeCount == root.val:
            self.count+=1
            
        return nodeSum,nodeCount
        
    
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        _,_ = self.sumAndCount(root)
        return self.count