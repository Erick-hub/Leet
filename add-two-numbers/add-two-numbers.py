# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1=l1
        p2=l2
        head=ListNode(None,None)
        p3=head
        carry=0
        s=0
        while p1 or p2:
            if p1 and p2:
                s=p1.val+p2.val+carry
                if s>=10:
                    p3.val=s%10
                    carry=s//10
                else:
                    p3.val=s
                    carry=0
                if p1.next or p2.next:
                    p3.next=ListNode(None,None)
                    p3=p3.next
                p1=p1.next
                p2=p2.next
            elif p1:
                s=p1.val+carry
                if s>=10:
                    p3.val=s%10
                    carry=s//10
                else:
                    p3.val=s
                    carry=0
                if p1.next:
                    p3.next=ListNode(None,None)
                    p3=p3.next
                p1=p1.next
            elif p2:
                s=p2.val+carry
                if s>=10:
                    p3.val=s%10
                    carry=s//10
                else:
                    p3.val=s
                    carry=0
                if p2.next:
                    p3.next=ListNode(None,None)
                    p3=p3.next
                p2=p2.next
        if carry:
            p3.next=ListNode(None,None)
            p3=p3.next
            p3.val=carry
        return head