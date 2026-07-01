# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        # helper function
        def mergeList(l1, l2):
            dummy = ListNode()
            tail = dummy

            while l1 and l2:
                if l1.val < l2.val:
                    tail.next = l1
                    l1 = l1.next
                else:
                    tail.next = l2
                    l2 = l2.next
                tail = tail.next

            if l1:
                tail.next = l1
            
            if l2:
                tail.next = l2
            
            return dummy.next
        
        # ensure lists not empty
        if not lists or len(lists) == 0:
            return None

        # Must have more than one list then we could do merge
        while len(lists) > 1:
            mergedList = []

            # each two lists merge into one list
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if (i+1) < len(lists) else None
                mergedList.append(mergeList(l1, l2))
            
            # update var lists with temp var mergedList
            lists = mergedList
        
        return lists[0]




