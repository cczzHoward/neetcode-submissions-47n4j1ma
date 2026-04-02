# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        stack = []
        cur = root

        while cur or stack:
            # 先往左側找 node (目標要從最小找到最大, 所以從最小開始)
            while cur:
                stack.append(cur)
                cur = cur.left

            # 處理 node (看是否是我們要找的第 k 小的 node)
            cur = stack.pop()
            n += 1
            if n == k:
                return cur.val

            # 順序 左 -> 中 -> 右
            #      完    完    未完
            cur = cur.right