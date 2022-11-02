# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.depthDict = {}
    
    
    def __levelOrder__(self, root, depth):
        if not root:
            return
        if depth not in self.depthDict:
            self.depthDict[depth] = []
            
        self.depthDict[depth].append(root.val)
        if root.left:
            self.__levelOrder__(root.left,depth+1)
            
        if root.right:
            self.__levelOrder__(root.right,depth+1)
    
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.__levelOrder__(root,0)
        result = []
        for i,k in enumerate(sorted(self.depthDict)):
            if i%2!=0:
                self.depthDict[k].reverse()
            result.append(self.depthDict[k])
        return result