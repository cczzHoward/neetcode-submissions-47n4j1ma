# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return [True, 0] #[是否balance, 高度]
            
            left = dfs(root.left)
            right = dfs(root.right)

            # 左邊所有子樹是否平衡 & 右邊所有子樹是否平衡 & 目前這棵樹是否平衡
            balanced = left[0] and right[0] and abs(left[1]-right[1]) <= 1

            return [balanced, 1 + max(left[1], right[1])]
        
        return dfs(root)[0]
