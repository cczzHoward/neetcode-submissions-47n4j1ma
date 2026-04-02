/**
 * Definition for singly-linked list.
 * class ListNode {
 *     constructor(val = 0, next = null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */

class Solution {
    /**
     * @param {ListNode} head
     * @return {void}
     */
    reorderList(head) {

        // 分割成兩個 Linked List
        let slow = head;
        let fast = head;
        while (fast.next && fast.next.next) {
            slow = slow.next;
            fast = fast.next.next;
        }
        
        // 將後半部分的 next 反轉 ( "->" 變成 "<-" )
        let curr = slow.next;
        slow.next = null;
        let prev = null;
        while (curr) {
            let nextNode = curr.next;
            curr.next = prev;
            prev = curr;
            curr = nextNode;
        }

        // 將前後段依序組合
        let p1 = head;
        let p2 = prev;
        while(p1 && p2) {
            let nextP1 = p1.next;
            let nextP2 = p2.next;
            p1.next = p2;
            p2.next = nextP1;
            p1 = nextP1;
            p2 = nextP2;
        }
    }
}
