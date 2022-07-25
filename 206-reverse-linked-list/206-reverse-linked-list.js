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
var reverseList = function(head, prev=null) {
    if(!head) return prev;
    let next = head.next; // 先把下一個記起來
    head.next = prev; // 將自己反過來指向前一個
    return reverseList(next, head);
};