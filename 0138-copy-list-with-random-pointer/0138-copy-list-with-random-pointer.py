"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return
        nodeMap = {}
        temp = head
        while temp:
            node = Node(temp.val)
            nodeMap[temp] = node
            temp = temp.next
           
        temp = head
        while temp:
            if temp.next:
                nodeMap[temp].next = nodeMap[temp.next]
            if temp.random:
                nodeMap[temp].random = nodeMap[temp.random]
            temp = temp.next
        
        return nodeMap[head]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         nodeMap = {}
#         temp = head
#         while temp:
#             nodeMap[temp] = Node(temp.val)
#             temp = temp.next
            
#         temp = head
#         while temp:
#             if temp.next:
#                 nodeMap[temp].next = nodeMap[temp.next]
#             temp = temp.next
            
#         temp = head
#         while temp:
#             if temp.random:
#                 nodeMap[temp].random = nodeMap[temp.random]
#             temp = temp.next
        
#         return nodeMap[head]