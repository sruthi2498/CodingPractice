# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict

class Solution:
    def __init__(self):
        self.counter = defaultdict(int)
        
    def __subtreSum__(self,root):
        if not root:
            return 0
        
        leftSum = self.__subtreSum__(root.left)
        rightSum = self.__subtreSum__(root.right)
        currSum = root.val+leftSum+rightSum
        self.counter[currSum]+=1
        return currSum
    
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        self.__subtreSum__(root)
        d = sorted(self.counter.items(), key = lambda x :x[1], reverse = True)
        result = []
        maxV = d[0][1]
        i = 0
        while i<len(d) and d[i][1]==maxV:
            result.append(d[i][0])
            i+=1
        return result
        