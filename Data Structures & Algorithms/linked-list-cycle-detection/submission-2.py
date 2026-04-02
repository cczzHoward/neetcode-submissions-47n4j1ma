# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head

        # 因為我們會取到 fast.next 這個 node 的 next
        # 所以要確定 fast.next 有沒有值，不然如果沒有值的話會報錯
        while fast and fast.next: 
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        
        return False