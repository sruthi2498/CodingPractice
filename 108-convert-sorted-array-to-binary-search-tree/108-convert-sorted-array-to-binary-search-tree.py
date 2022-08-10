# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBST(self,  nums: List[int]) -> Optional[TreeNode]:
        n = len(nums)
        if n==0:
            return None
        if n==1:
            return TreeNode(nums[0])
        
        mid = n//2
        # print("root",nums[mid])
        root = TreeNode(nums[mid])
        root.left = self.createBST(nums[:mid])
        root.right = self.createBST(nums[mid+1:])
        return root
        
        
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.createBST(nums)