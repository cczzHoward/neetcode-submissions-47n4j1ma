# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        # 讓 left right 拉出 n 的長度
        while n > 0 and right:
            right = right.next
            n -= 1
        
        # 這樣走到 linked-list 尾巴的時候 left 的下一個 node 就會是要刪除的 node
        while right:
            left = left.next
            right = right.next
        
        # 跳過那一個 node 等於 刪除 node
        left.next = left.next.next
        return dummy.next