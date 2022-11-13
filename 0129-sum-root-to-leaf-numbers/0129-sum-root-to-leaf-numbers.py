# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = []
    def getNum(self,digits):
        n = len(digits)
        k = 0
        i = n-1
        num = 0
        while i>=0:
            num += digits[i]* (10**k)
            k+=1
            i-=1
        return num
    def getAllPaths(self,root,paths):
        if not root:
            return paths
        if not root.left and not root.right:
            
            self.res.append(self.getNum(paths))
        # print(paths)
        left_paths = self.getAllPaths(root.left,paths+[root.left.val]) if root.left else []
        right_paths = self.getAllPaths(root.right,paths+[root.right.val]) if root.right else []
        return left_paths+right_paths
        
    
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        paths = self.getAllPaths(root,[root.val])
        print(self.res)
        return sum(self.res)