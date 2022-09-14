# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        prev = node
        temp = prev.next
        while temp and temp.next:
            print("prev ",prev.val, "temp ",temp.val)
            prev.val = temp.val
            prev = temp
            temp = temp.next
        print("prev ",prev.val, "temp ",temp.val)
            
        if not temp:
            prev = None 
        else:
            prev.val = temp.val
            prev.next = None
        