# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = collections.deque([root])

        while q:
            qLen = len(q)
            rightSide = None

            # 跑每一層 tree
            for i in range(qLen):
                node = q.popleft()
                if node:
                    # 最後拿到的 rightSide 一定會是 level 的最右側 node
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)
                
            if rightSide:
                    res.append(rightSide.val)
            
        return res
