# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        s = 0
        temp = head
        while temp!=None:
            s+=1
            temp = temp.next
        # print(s)
        n = s-n+1
        # print(n)
        if n==0:
            return head
        if n==1:
            return head.next
        
        temp = head
        prev = None
        count = 1
        while count<n:
            prev = temp
            temp = temp.next
            count+=1
        prev.next = temp.next
        return head
            
        