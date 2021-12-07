# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        
        id_list=[]
        current=head
        while current:           
            nxt=current.next
            id_list.append(id(current))
            if nxt:
                if id(nxt) in id_list:
                    return True
                current=nxt
            else:
                return False
            