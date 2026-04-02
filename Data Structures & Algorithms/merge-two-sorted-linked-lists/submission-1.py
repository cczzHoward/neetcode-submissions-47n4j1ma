# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        answerList = ListNode()
        currentN = answerList

        while (list1 and list2):
            if (list1.val <= list2.val):
                currentN.next = list1
                list1 = list1.next
            else:
                currentN.next = list2
                list2 = list2.next
            currentN = currentN.next

        if (list1):
            currentN.next = list1
        else:
            currentN.next = list2

        return answerList.next        