# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start=head
        current=head
        while current:
            nex=current.next            
            if nex:
                while nex.val==current.val:
                    nex=nex.next
                    if not nex:
                        break
                current.next=nex
                current=nex
            else:
                current.next=nex
                current=nex
        return head        
         