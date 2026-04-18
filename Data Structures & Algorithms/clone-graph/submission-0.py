"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}

        def dfs(node):
            # 算是 cache 的概念吧
            if node in oldToNew:
                return oldToNew[node]
            
            # hard copy
            copy = Node(node.val)
            oldToNew[node] = copy
            # 把該 node 所有 neighbor hard copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            # 回傳該 node
            return copy

        # 從任何一個 node 理論上都可以輸出整個 graph
        return dfs(node) if node else None