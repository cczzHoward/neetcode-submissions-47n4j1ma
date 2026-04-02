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
     * @param {ListNode} list1
     * @param {ListNode} list2
     * @return {ListNode}
     */
    mergeTwoLists(list1, list2) {
        let answerList = new ListNode();
        let currentN = answerList;

        while (list1 && list2) {
            if (list1.val <= list2.val) {
                currentN.next = list1;
                list1 = list1.next;
            } else {
                currentN.next = list2;
                list2 = list2.next;
            }
            currentN = currentN.next;
        }

        currentN.next = list1 || list2;
        return answerList.next;
    }
}
