# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: return True
        if not root: return False

        if self.is_same_tree(root, subRoot): return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    

    def is_same_tree(self, a_root, b_root):
        if not a_root and not b_root:
            return True

        if a_root and b_root and a_root.val == b_root.val:
            return self.is_same_tree(a_root.left, b_root.left) and self.is_same_tree(a_root.right, b_root.right)
        
        return False