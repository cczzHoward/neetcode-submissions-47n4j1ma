"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # 預設有 None: None 這個 pair 是因為在 copy 的時候如果 next, random 其中一個指向 None 的話沒有這個 pair 會報錯
        old_to_copy = {None: None} # pair: oldNode -> newNode

        # create copy node and let oldNode map to newNode
        cur = head
        while cur:
            copy = Node(cur.val)
            old_to_copy[cur] = copy
            cur = cur.next
        
        # add next and random to each newNode
        cur = head
        while cur:
            copy = old_to_copy[cur]
            copy.next = old_to_copy[cur.next]
            copy.random = old_to_copy[cur.random]
            cur = cur.next
        
        return old_to_copy[head]

        