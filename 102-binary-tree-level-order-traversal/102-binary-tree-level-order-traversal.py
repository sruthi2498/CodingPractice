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
    
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.__levelOrder__(root,0)
        result = []
        for k in sorted(self.depthDict):
            result.append(self.depthDict[k])
        return result
#         if not root:
#             return []
#         queue=["|",root,"|"]
#         result =[]
#         l=[]
#         while len(queue)>0:
#             if queue.pop(0)=="|":
#                 l=[]
#                 while len(queue)>0 and queue[0]!="|":
#                     nextNode = queue.pop(0)
#                     l.append(nextNode.val)
#                     if nextNode.left:
#                         queue.append(nextNode.left)
#                     if nextNode.right:
#                         queue.append(nextNode.right)
#                 if l:
#                     result.append(l)
#                     queue.append("|")
#         return result
        