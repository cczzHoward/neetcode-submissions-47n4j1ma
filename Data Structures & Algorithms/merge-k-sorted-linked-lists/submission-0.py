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
        
        # 確保 lists 不是空串列
        if not lists or len(lists) == 0:
            return None
        
        # 確認 list 含有一個以上 -> 才可以做合併
        while len(lists) > 1:
            mergedLists = []
            
            # 每兩個 lists 合併成一個
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if (i+1)<len(lists) else None
                mergedLists.append(mergeList(l1, l2))
            
            # 把合併完畢的結果存進 lists 裡面
            lists = mergedLists

        # 合併結束回傳結果
        return lists[0]












