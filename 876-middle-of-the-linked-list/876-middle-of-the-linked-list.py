# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        c = 0
        temp = head
        while temp!=None:
            temp=temp.next
            c+=1
        
        m = c//2
        # print(c,m)
        i = 0
        temp = head
        while temp!=None and i<m:
            temp=temp.next
            i+=1
        return temp