# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        first = head.next 
        if not first:
            return head
        
        while first!=None:
            second = first.next 
            while second!=None and second.val!=0:
                first.val+=second.val
                second = second.next 
            first.next = second.next
            first = first.next
            
                
        return head.next