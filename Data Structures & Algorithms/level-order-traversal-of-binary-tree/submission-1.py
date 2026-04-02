# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        queue = []
        queue.append(root)

        while queue:
            q_len = len(queue)
            tmp = []
            for i in range(q_len):
                cur_node = queue.pop(0)
                if cur_node:
                    tmp.append(cur_node.val)
                    queue.append(cur_node.left)
                    queue.append(cur_node.right)
            if tmp: res.append(tmp)

        return res        