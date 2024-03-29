/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseList = function (head) {
    if(head==null || !head.next==null){
        return head
    }
    else{
        let current=head   
        let prev=null
        let nxt=null
        while(current){
            nxt=current.next
            current.next=prev
            prev=current        
            current=nxt
            head=prev
            
        }
        return head
    }
};