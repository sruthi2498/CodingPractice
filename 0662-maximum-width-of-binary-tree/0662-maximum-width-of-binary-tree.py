# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.depthDict = {}
    
    def __levelOrder__(self, root, depth, num):
        if depth not in self.depthDict:
            self.depthDict[depth] = []
        if not root:
            return
        
        self.depthDict[depth].append([root.val,num])
        if root.left:
            self.__levelOrder__(root.left,depth+1, 2*num)
        
        if root.right:
            self.__levelOrder__(root.right,depth+1, 2*num+1)
    
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.__levelOrder__(root,0,1)
        maxWidth= 0
        for k,v in self.depthDict.items():
            if(v[-1][1]-v[0][1]+1> maxWidth):
                maxWidth =v[-1][1]-v[0][1]+1
        return maxWidth