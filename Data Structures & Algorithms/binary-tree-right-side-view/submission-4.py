# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        queue = collections.deque([root])

        while queue:
            q_length = len(queue)
            right_most_node = None

            for _ in range(q_length):
                cur_node = queue.popleft()

                if cur_node:
                    right_most_node = cur_node
                    queue.append(cur_node.left)
                    queue.append(cur_node.right)
            
            if right_most_node:
                res.append(right_most_node.val)
        
        return res

