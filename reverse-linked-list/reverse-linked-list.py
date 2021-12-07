# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            if head.next:
                prev=None
                current=head
                
                while current:
                    nxt=current.next
                    current.next=prev
                    prev=current
                    current=nxt
                head=prev
                return head
            else:              
                return head 
        else:
            return None