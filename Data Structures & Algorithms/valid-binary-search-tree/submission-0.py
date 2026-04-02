# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, left, right):
            if not node:
                return True
            
            # 看這個 node 是否符合 BST
            # 不符回傳 False
            if not (node.val > left and node.val < right):
                return False

            # 符合則繼續往下找
            return (valid(node.left, left, node.val) and
                    valid(node.right, node.val, right))
        
        return valid(root, float("-inf"), float("inf"))